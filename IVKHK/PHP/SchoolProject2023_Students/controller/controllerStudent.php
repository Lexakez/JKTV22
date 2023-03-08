<?php
class controllerStudent
{

    //-------------add student form
    public static function addStudentForm()
    {
        //получить список специальностей для формы add student
        $rows = Model::getSpecialityList();
        include_once('view/addStudentForm.php');
    }
    //-------------add student result
    public static function addStudentResult()
    {
        //получить список специальностей для формы add student
        $result = modelStudent::addStudent();
        $_SESSION['result'] =$result;
        header('Location:result');
    }

    public static function viewResult()
    {
        include_once('view/queryResult.php');
    }
    //-------------edit student form
    public static function editStudentForm($id)
    {
        //получить список специальностей для формы edit student
        $rows = Model::getSpecialityList();//spisok spec
        $student = Model::getStudentDetail($id);//dannye studenta
        include_once('view/editStudentForm.php');
    }
    //-----------edit student result
    public static function editStudentResult($id)
    {
        $result = modelStudent::editStudent($id);
        $_SESSION['result'] = $result;
        header('Location:result');
    }
    public static function deleteStudentForm($id)
    {
        $student = Model::getStudentDetail($id);//dannye studenta
        include_once('view/deleteStudentForm.php');
    }
    //-----------delete student result
    public static function deleteStudentResult($id)
    {
        $result = modelStudent::deleteStudent($id);
        $_SESSION['result'] = $result;
        header('Location:result');
    }
}
?>