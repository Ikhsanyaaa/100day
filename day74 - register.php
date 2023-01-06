<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Login Taskey</title>
	<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
	<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
	<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
</head>
<body>
	<div class="sidenav">
         <div class="login-main-text">
            <h2>Taskey</h2>
            <p>The key from your task.</p>
         </div>
      </div>
      <div class="main">
         <div class="col-md-6 col-sm-12">
            <div class="login-form">
               <form>
                    <div class="form-group">
                        <label>Nama lengkap</label>
                        <input type="text" class="form-control" placeholder="Nama lengkap">
                    </div>
                    <div class="form-group">
                        <label>Universitas</label>
                        <input type="text" class="form-control" placeholder="Universitas">
                    </div>
                    <div class="form-group">
                        <label>Jurusan</label>
                        <input type="text" class="form-control" placeholder="Jurusan">
                    </div>
                  <div class="form-group">  
                     <label>Username</label>
                     <input type="text" class="form-control" placeholder="UserName">
                  </div>
                  <div class="form-group">
                     <label>Password</label>
                     <input type="password" class="form-control" placeholder="Password">
                  </div>
                  <a class="btn btn-dark" href="index.php" role="button">Daftar</a>
               </form>
            </div>
         </div>
      </div>
      <style type="text/css">
      	body {
    font-family: "Lato", sans-serif;
}



.main-head{
    height: 150px;
    background: #FFF;
   
}

.sidenav {
    height: 100%;
    background-color: #202020;
    overflow-x: hidden;
    padding-top: 20px;
}


.main {
    padding: 0px 10px;
}

@media screen and (max-height: 450px) {
    .sidenav {padding-top: 15px;}
}

@media screen and (max-width: 450px) {
    .login-form{
        margin-top: 10%;
    }

    .register-form{
        margin-top: 10%;
    }
}

@media screen and (min-width: 768px){
    .main{
        margin-left: 40%; 
    }

    .sidenav{
        width: 40%;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
    }

    .login-form{
        margin-top: 40%;
    }

    .register-form{
        margin-top: 60%;
    }
}


.login-main-text{
    margin-top: 20%;
    padding: 60px;
    color: #fff;
}

.login-main-text h2{
    font-weight: 300;
}

.btn-black{
    background-color: #000 !important;
    color: #fff;
}
      </style>
</body>
</html>