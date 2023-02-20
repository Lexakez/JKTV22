<?php
    ob_start();
?>

<h2 class="text-center m-4">Student details speciality -
<?php echo $student['nameSpec']; ?>
</h2>

<div class="row">
    <div class="col-sm-3">
    <div class="flex-column ms-5 nav">
        <?php
        foreach ($specialityList as $spec){
            echo '<div class="nav-item">
                    <a class="nav-link" href="studByspec?id='.$spec['id'].'">'.$spec['nameSpec'].'</a>
                </div>';
        }
        ?>
    </div>
    </div>
    <div class="col-sm-9 mt-3">
        <div class="container">
            <div class="card">
                <div class="container-fliud">
                    <div class="wrapper row">
                    <?php
                        echo '<div class="col-md-4">
                                <img src="images/'.$student['photo'].'" />
                            </div>
                            <div class="col-md-8" style="margin-left: 20px; width: 500px;">
                                <h3>First name - '.$student['firstName'].'</h3>
                                <p> Date of Birth: '.$student['dataBirth'].'</p>
                                <p> Gender: '.$student['gender'].'</p>
                                <p> Address: '.$student['address'].'</p>
                                <p> Phone: '.$student['mobil'].'</p>
                                <h5> Speciality: '.$student['nameSpec'].'</h5>
                                <p> Year of study: '.$student['year'].'</p>
                                <p> <a href="students"> Back student list</a></p>
                            </div>';
                    ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<?php
    $content = ob_get_clean();
    include "view/templates/layout.php";
?>