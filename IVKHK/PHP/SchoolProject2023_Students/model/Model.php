<?php
/* для выборки данных из базы данных используем запросы,
 * class database из папки inc
 */
class Model {
	
    public static function getSpecialityList(){
        $query = "SELECT * FROM `speciality` ORDER BY `nameSpec`";
        $db = new database();
        $item = $db->getAll($query);
        return $item;
    }
    
    public static function getStudentList(){
        $query = "SELECT speciality.nameSpec, student.* FROM `speciality`,`student` WHERE speciality.id = student.specid ORDER BY speciality.nameSpec ASC,student.firstName ASC;";
        $db = new database();
        $item = $db -> getAll($query);
        return $item;
    }
    public static function getSpecialityDetail($id){
        $query = "SELECT * FROM `speciality` WHERE `id` =".$id;
        $db = new database();
        $item = $db->getOne($query);
        return $item;
    }
    public static function getStudentListByspec($id){
        $sql = "SELECT speciality.nameSpec, student.* FROM `speciality`,`student` WHERE speciality.id = student.specid AND speciality.id = $id ORDER BY student.firstName ASC";
        $db = new database();
        $item = $db->getAll($sql);
        return $item;
    }
    public static function getStudentDetail($id){
        $query = "SELECT speciality.nameSpec, student.* FROM `speciality`,`student` WHERE speciality.id=student.specid AND student.id=".$id;
        $db = new database();
        $item = $db->getOne($query);
        return $item;
    }
	
}//END CLASS
?>