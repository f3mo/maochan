<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8" />
    <title>App</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script charset="utf-8" src="js/app.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
<style>
body,html{
    height:100%;
}

</style>

</head>
<body>
<div class="container h-100 ">
  <div class="row h-100 justify-content-center align-items-center" action={{url_for('home')}}>
    <form class="col-8" method="post">
    <div class="input-group mb-3">
      <input type="text" name="url" class="form-control " placeholder="Paste URL" aria-label="Recipient's username" aria-describedby="basic-addon2">
          <div class="input-group-append">
             <input type="submit" class="btn btn-primary" value="shorten"></input>
          </div>
    </div>
{% if short_url %}
<div class="alert alert-success" role="alert">
 <a href="/{{ short_url }}">{{request.url +  short_url }}</a> 
</div>
{% endif  %}
    </form>   

  </div>  
</div>
</body>
</html>
