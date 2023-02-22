<!DOCTYPE>
<html>
    <head>
        <title>Estonian Hotels</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<!--скопируйте ссылку из файла header.php проект FormContact - для формы обратной связи   -->		
		<link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
        <link href="public/css/style.css" rel="stylesheet" type="text/css"/>        
    </head>
    <body>
	<div class="myBody">
        <header>
			<h2 class="myH">Estonian Hotels</h2>
			<ul class="myul">					
				<!--меню - навигация -->
                <li><a href="./">Home</a></li>
                <li><a href="cities">Hotels in Estonia</a></li>
                <li><a href="contact">Contact</a></li>
			</ul>
        </header>        
        <main>          
            <div class="content" > 
				<div id="content" style="padding-top:20px;">
					
					<!--изменяющийся контент сайта - содержание страни-->	
					<?php
                    if(isset($content)) echo $content;
                    ?>
				</div>
            </div><!-- end content --> 
        </main>        
        <footer>
            <p class="footer">&copy; 2021 Design IVKHK<p>
        </footer>
       </div> 
    </body>
</html>












