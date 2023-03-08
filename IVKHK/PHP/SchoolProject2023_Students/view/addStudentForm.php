<?php
ob_start();
?>
<h2 class="text-center m-4"> Add new student</h2>
<div class="container">
    <form action="addstudentResult" method="POST" enctype="multipart/form-data">
        <div class="row">
            <div class="col-sm-6">
                <div class="form-outline mb-2">
            <label class="form-label">First Name</label>
            <input type="text" name="firstName" class="form-control" required />
        </div>
         <div class="form-outline mb-2">
            <label class="form-label">Birth Date</label>
            <input type="date" name="dateBirth" class="form-control" required />
        </div>
            <div class="form-outline mb-2">
                <label class="form-label">Gender</label>
                <div class="btn-group-sm form-control" role="group" aria-label="Basic radio toggle button group">
                    <input type="radio" class="btn-check" name="gender" id="btnradio1" autocomplete="off" value="m">
                    <label class="btn btn-outline-primary" for="btnradio1">Male</label>

                    <input type="radio" class="btn-check" name="gender" id="btnradio2" autocomplete="off" value="n">
                    <label class="btn btn-outline-primary" for="btnradio2">Female</label>
                </div>
            </div>
        <div class="form-outline mb-2">
            <label class="form-label">Address</label>
            <input type="text" name="address" class="form-control" required />
        </div>
        <div class="form-outline mb-2">
            <label class="form-label">Year</label>
            <input type="text" name="year" class="form-control" required />
        </div>    
       
        <div class="form-outline mb-2">
            <label class="form-label">Mobil</label>
            <input type="tel" name="mobil" class="form-control" required />
        </div>
        <div class="form-outline mb-2">
            <label class="form-label">Picture</label>
            <input type="file" name="picture" class="form-control" required/>
        </div>
            <div class="form-outline mb-2">
                <label class="form-label"> Speciality select</label>
                <select class="form-select" name="specId">
                    <?php
                    foreach ($rows as $row) {
                        echo '<option value="'.$row['id'].'">'.$row['nameSpec'].'</option>';
                    }
                    ?>
                </select>
            </div>
        </div>
         <div class="form-outline mb-2">
        <a role="button" class="btn btn-primary" href="students">Back student list</a>
         </div>
         <div class="form-outline mb-2">
            <button type="submit" class="btn btn-primary" name="save">Add student</button>
        </div>
<?php
$content = ob_get_clean();
include "view/templates/layout.php";
?>