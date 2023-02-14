<?php
    ob_start();
?>

<h2 class="text-center m-4"> Student list
    <?php
        $speciality=isset($specialityDetail) ? $specialityDetail['nameSpec']:'';
        echo 'by '.$speciality.' speciality'
    ?>
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
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>First name</th>
                    <th>Date of birth</th>
                    <th>Year of study</th>
                    <th>Speciality</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php
                    $n=0;
                    foreach ($studentList as $student){
                        $n++;
                        echo '<tr>
                            <th>'.$n.'</th>
                            <td>'.$student['firstName'].'</td>
                            <td>'.$student['dataBirth'].'</td>
                            <td>'.$student['year'].'</td>
                            <td>'.$student['nameSpec'].'</td>
                            <td><a href="student?id='.$student['id'].'">Details</a></td>
                            </tr>';
                    }
                ?>
            </tbody>
        </table>
        <p class="text-end me-5"> Count of list
            <?php
                echo count($studentList);
            ?>
        </p>
    </div>
</div>
<?php
    $content=ob_get_clean();
    include "view/templates/layout.php";
?>