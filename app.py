from flask import Flask, render_template, request, url_for , redirect
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/url.db'
db = SQLAlchemy(app)

class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String, unique=True, nullable=False)


try:
    db.create_all()
except:
    pass



@app.route('/' ,methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        hash  = md5(url.encode())
        short = hash.hexdigest()[0:7]
        post = Url(url=url,short_url=short)
        db.session.add(post)
        db.session.commit()
        short = Url.query.filter_by(url=url).first()
        return render_template('index.tpl', short_url=short.short_url)
    return render_template('index.tpl')

#API


@app.route('/api', methods=['POST', 'GET'])
def api():
    purl  = ''
    for v in request.form.keys():
        purl = v
    hash  = md5(purl.encode())
    short = hash.hexdigest()[0:7]
    print(purl, short)
    post = Url(url=purl,short_url=short)
    db.session.add(post)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    short = Url.query.filter_by(url=purl).first()
    url = f"{request.base_url}/{short.short_url}\n"
    url = url.replace('api/','')
    return url

@app.route('/<short>')
def shorty(short):
    url = Url.query.filter_by(short_url = short).first()
    short = url.short_url
    return redirect(url.url)


if __name__ == '__main__':
    app.run(debug=True)
