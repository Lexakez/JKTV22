<!DOCTYPE html>
<html lang="ru">
  <head>    
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Project School</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
	 <link href="public/css/style.css" rel="stylesheet">
  </head>

  <body class="d-flex flex-column h-100">  
	<nav class="navbar navbar-expand-md navbar-light  bg-light   sticky-top">
	  <div class="container">
		<a href="" class="navbar-brand">Project School</a>
			<button type="button" class="navbar-toggler collapsed" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
				<span class="navbar-toggler-icon"></span>
			</button>
		  
		  <div class="navbar-collapse collapse" id="collapsibleNavbar">
			  <div class="me-auto navbar-nav">
				  <a href="./"  class="nav-link">Specialities</a>
				  <a href="students"  class="nav-link">Students</a>			  
				  <a href="blog"  class="nav-link">Blog</a>			  
			  </div>
			  <form class="d-flex" method="GET" action="search">
				  <input placeholder="search" type="text" name="text" class="me-sm-2 form-control">
				  <button type="submit" class="btn btn-outline-success">Search</button>
			  </form>
			  <div class="me-auto navbar-nav">
				<?php
				if(!isset($_SESSION['userId'])){
					?>
				  		<a href="login"  class="nav-link">Login</a>
				  		<a href="register"  class="nav-link">Register</a>
					<?php } elseif (isset($_SESSION['userId'])) {
					?>
						<div class="dropdown ms-5">
							<a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
								<?php echo $_SESSION['name'] ?>
							</a>
							<ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
								<li><a class="dropdown-item" href="logout">Log out</a></li>
								<li><a class="dropdown-item" href="profile">Profile</a></li>
							</ul>
						</div>
					<?php } ?>	
			  </div>
		  </div>
	  </div>
	</nav>  
	<!-- content start-->
	<div class="mt-3 container" style="min-height:600px; height:100%;">
		<!--        php content      -->
		<?php
		if(isset($content)){
			echo $content;
		}
		?>
	</div>
	<!-- content end-->
	
	<!-- footer start-->	
	<footer class="main-footer">
		<div class="text-center">
			<strong>Project School | IVKHK | Jõhvi | 2023</strong>
		</div>
	</footer>
	
</body>
</html>