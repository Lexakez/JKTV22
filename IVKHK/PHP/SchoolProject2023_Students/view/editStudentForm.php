<?php
ob_start();
?>
<h2 class="text-center m-4"> Edit student data</h2>
<div class="container">
    <form action="editstudentResult?id=<?php echo $id; ?>" method="POST" enctype="multipart/form-data">
        <div class="row">
            <div class="col-sm-6">
                <div class="form-outline mb-2">
            <label class="form-label">First Name</label>
            <input type="text" name="firstName" class="form-control" required value="<?php echo $student['firstName'];?>"/>
        </div>
       
         <div class="form-outline mb-2">
            <label class="form-label">Birth Date</label>
            <input type="date" name="dateBirth" class="form-control" required value="<?php echo $student['dateBirth'];?>"/>
        </div>
        <!-- Gender input -->
            <div class="form-outline mb-2">
                <label class="form-label">Gender</label>
                <div class="btn-group-sm form-control" role="group" aria-label="Basic radio toggle button group">
                    <input type="radio" class="btn-check" name="gender" id="btnradio1" autocomplete="off" 
                    <?php if($student['gender'] == 'm') echo 'checked';?> value="m">
                    <label class="btn btn-outline-primary" for="btnradio1">Male</label>

                    <input type="radio" class="btn-check" name="gender" id="btnradio2" autocomplete="off" 
                    <?php echo $check = $student['gender'] == 'n' ? 'checked' : '';?> value="n">
                    <label class="btn btn-outline-primary" for="btnradio2">Female</label>
                </div>
            </div>
        <div class="form-outline mb-2">
            <label class="form-label">Address</label>
            <input type="text" name="address" class="form-control" required value="<?php echo $student['address'];?>"/>
        </div>
        <div class="form-outline mb-2">
            <label class="form-label">Year</label>
            <input type="text" name="year" class="form-control" required value="<?php echo $student['year'];?>"/>
        </div>    
        <!-- picture input -->
            
       
        <div class="form-outline mb-2">
            <label class="form-label">Mobil</label>
            <input type="tel" name="mobil" class="form-control" required value="<?php echo $student['mobil'];?>"/>
        </div>
        <div class="form-outline mb-2">
            <label class="form-label">OldPicture</label>
            <input type="text" name="oldpicture" readonly value="<?php echo $student['photo']; ?>"/>
            <img src="images/<?php echo $student['photo']; ?>" width="7%" />

            <br><label class="form-label">Picture</label>
            <input type="file" name="picture" class="form-controll" />
        </div>
            <!-- Speciality id -->
            <div class="form-outline mb-2">
                <label class="form-label"> Speciality select</label>
                <select class="form-select" name="specId">
                    <?php
                    foreach ($rows as $row) {
                        echo '<option value="'.$row['id'].'"';
                        if($row['id'] == $student['specId']) echo ' selected';
                        echo '>'.$row['nameSpec'].'</option>';
                    }
                    ?>
                </select>
            </div>
        </div>
         <div class="form-outline mb-2">
        <a role="button" class="btn btn-primary" href="students">Back student list</a>
         </div>
         <div class="form-outline mb-2">
            <button type="submit" class="btn btn-primary" name="save">Edit student data</button>
        </div>
<?php
$content = ob_get_clean();
include "view/templates/layout.php";
?>