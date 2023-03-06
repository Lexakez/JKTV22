<?php
    ob_start();
?>

<h2 class="text-center m-4">Blog</h2>
<p class="text-end me-5"> Count of post 
    <?php
            echo count($postList)." records";
            ?> 
             </p>
            <?php
            if (isset($text)) echo '<h4>Результат поиска по запросу '.$text.'</h4>';
            ?>
           
      
<div class="row">
    
    <div class="col-sm-9 mt-3">
        <?php
        if(count($postList)>0){
        ?>
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Image</th>
                    <th>Theme</th>
                    <th>Description</th>
                    <th>Date of publish</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $n=0;
                foreach ($postList as $post) {
                    $n++;
                    echo '<tr>
                        <th>'.$n.'</th>
                        <td><img width=200px,height=150px src="'.$post['image'].'">
                        <td>'.$post['title'].'</td>
                        <td><div><p style="width:200px" class="clip">'.$post['description'].'"</p></div></td>
                        <td>'.$post['date'].'</td>
                        <td><a href="posts?id='.$post['id'].'">Details</a></td>
                    </tr>';
                }
                ?>

            </tbody>
        </table>
        <?php
        }
        ?>
    </div>
    <div class="col-sm-3 mt-3">
        <div class="flex-column me-2 nav">
            <?php
            foreach ($calendar as $cal) {
                echo '<div class="nav-item">
                <a class="nav-link" href="cal?id='.$cal['form'].'">'.$cal['form'].'</a> </div>';
            }
            ?>
		</div>
    </div>
</div>
<?php
    $content = ob_get_clean();
    include "view/templates/layout.php";
?>