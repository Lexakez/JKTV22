<?php
    ob_start();
?>

<h2 class="text-center m-4">Post detail
    <?php //echo $post['nameSpec']; ?>
</h2>

<div class="row">
    
    <div class="col-sm-12 mt-3">
        
            <div class="card">
                <div class="container-fluid  my-5">
                    <div class="wrapper row">
                        <?php
                        echo '<div class="col-md-4">
                                <img src="'.$post['image'].'" class="img-fluid" />
                            </div>
                            <div class="col-md-8">
                                <h3>Theme - '.$post['title'].'</h3>
                                <p>Description: '.$post['description'].'</p>
                                <p>Date of publish: '.$post['date'].'</p>
                                <p> <a href="blog">Back blog</a></p>
                            </div>';
                        ?>
                    </div>
                </div>
            </div>
       
    </div>
</div>
<?php
    $content = ob_get_clean();
    include "view/templates/layout.php";
?>