from flask import Flask, render_template, request, url_for , redirect
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
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
        short = uuid4().hex[:7]
        post = Url(url=url,short_url=short)
        db.session.add(post)
        db.session.commit()
        short = Url.query.filter_by(url=url).first()
        return render_template('index.tpl', short_url=short.short_url)
    return render_template('index.tpl')


@app.route('/<short>')
def shorty(short):
    url = Url.query.filter_by(short_url = short).first()
    short = url.short_url
    return redirect(url.url)


if __name__ == '__main__':
    app.run(debug=True)
