<?php
class modelStudent
{
    public static function addStudent()
    {
        $result = false;
        if (isset($_POST['save'])) {
            // Читаем данные из формы
            $firstName = $_POST['firstName'];
            $dateBirth = $_POST['dateBirth'];
            $address = $_POST['address'];
            $gender = $_POST['gender'];
            $year = $_POST['year'];
            $mobil = $_POST['mobil'];
            $specId = $_POST['specId'];
            // Закачка картинки на сервер
            $photo = $_FILES['picture']['name'];//
            if ($photo != "") {
                $uploadfile = 'images/'. basename($_FILES['picture']['name']);
                move_uploaded_file($_FILES['picture']['tmp_name'], $uploadfile);
            }
            //-------------- zapros INSERT table students --------------------------------
            $sql ="INSERT INTO `student` (`id`, `firstName`, `dateBirth`, `gender`, `address`, `year`, `mobil`, `photo`, `specId`)  VALUES(NULL, '$firstName','$dateBirth','$gender','$address','$year','$mobil','$photo','$specId')";
				 
            $database = new database();
            $item = $database->executeRun($sql);//result insert
            if ($item == true) {
                $result = true;
            }
        }// end if pressed seva button
        return $result;
    }// end function add
    //---------------
    public static function editStudent($id)
    {
        $result = false;
        if (isset($_POST['save'])) {
            // Читаем данные из формы
            $firstName = $_POST['firstName'];
            $dateBirth = $_POST['dateBirth'];
            $address = $_POST['address'];
            $gender = $_POST['gender'];
            $year = $_POST['year'];
            $mobil = $_POST['mobil'];
            $specId = $_POST['specId'];
            $oldphoto = $_POST['oldpicture'];
            // Закачка картинки на сервер
            $photo = $_FILES['picture']['name'];//new picture
            if ($photo != "" and $photo != $oldphoto) {
                $uploadfile = 'images/'. basename($_FILES['picture']['name']);
                move_uploaded_file($_FILES['picture']['tmp_name'], $uploadfile);
                unlink("images/".$oldphoto);//delete old photo
            } else {
                $photo=$oldphoto;//ostavlyaem old photo
            }
            //-------------- zapros UPDATE table students --------------------------------
            $sql ="UPDATE `student` SET `firstName` = '$firstName', `dateBirth` = '$dateBirth', `gender` = '$gender', `address` = '$address', `year` = '$year', `mobil` = '$mobil', `photo` = '$photo', `specId` = '$specId' WHERE `student`.`id` = $id";
            $database = new database();
            $item = $database->executeRun($sql);//result UPDATE
            if ($item == true) {
                $result = true;
            }
        }// end if pressed save button
        return $result;
    }// end function add
    //-------------------------------delete student 
    public static function deleteStudent($id)
    {
        $result = false;
        $sql = "DELETE FROM `student` WHERE `student`.`id` = $id";
        $database = new database();
        $item = $database->executeRun($sql);
        if ($item == true) {
            $result = true;
        } //item
        return $result;
    }// end function delete
}//end class
?>