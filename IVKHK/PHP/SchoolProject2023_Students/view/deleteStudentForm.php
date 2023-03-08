<?php
    ob_start();
?>

<h2 class="text-center m-4">Student details speciality -
    <?php echo $student['nameSpec']; ?>
</h2>

<div class="row">
    <div class="col-sm-3">
    <div class="flex-column ms-5 nav">

    </div>
    </div>
    <div class="col-sm-9 mt-3">
        <div class="container">
            <div class="card">
                <div class="container-fluid">
                    <div class="wrapper row">
                        <?php
                        echo '<div class="col-md-4">
                                <img src="images/'.$student['photo'].'" />
                            </div>
                            <div class="col-md-8">
                                <h3>First name - '.$student['firstName'].'</h3>
                                <p>Date of Birth: '.$student['dateBirth'].'</p>
                                <p>Gender: '.$student['gender'].'</p>
                                <p>Address: '.$student['address'].'</p>
                                <p>Phone: '.$student['mobil'].'</p>
                                <h5>Speciality: '.$student['nameSpec'].'</h5>
                                <p>Year of study: '.$student['year'].'</p>
                                <p>
                                <a type="button" class="btn btn-primary btn-block mb-4" href="deletestudentResult?id='.$student['id'].'">Delete student data</a>
                                <a type="button" class="btn btn-primary btn-block mb-4" href="students">Back student list</a>
                                </p>
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