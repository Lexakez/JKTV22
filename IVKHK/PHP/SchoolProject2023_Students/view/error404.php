<?php 
	ob_start();
	
 ?>
 
	<div class="container text-center"  style="width:80%; ">
		<img src="images/404.png" >    
	</div> 

<?php 
	$content = ob_get_clean(); 
	include "view/templates/layout.php";
?>