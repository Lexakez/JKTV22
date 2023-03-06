<?php
class Controller { 
    public static function StartSite(){
        $specialityList = Model::getSpecialityList();
        include_once('view/homepage.php');
        return;
    }
    public static function error404(){
        include_once('view/error404.php');
        return;
    }
    public static function StudentList(){
        $specialityList = Model::getSpecialityList();
        $studentList = Model::getStudentList();
        include_once('view/studentlist.php');
        return;
    }
    public static function StudentByspec($id){
        $specialityList = Model::getSpecialityList();
        $specialityDetail = Model::getSpecialityDetail($id);
        $studentList=Model::getStudentListByspec($id);
        include_once('view/studentlist.php');
        return;
    }
    public static function StudentDetail($id){
        $specialityList = Model::getSpecialityList();
        $student = Model::getStudentDetail($id);
        include_once('view/studentdetail.php');
        return;
    }
    public static function PostList() {
        $postList=Model::getPostsList();
        $calendar = Model::getCalendarik();
        include_once('view/postslist.php');
        return ;
    }
    public static function Calendar($id) {
        $postList = Model::getCalendar($id);
        $calendar = Model::getCalendarik();
        include_once('view/postslist.php');
        return;
    }
    public static function PostDetail($id) {

        $post = Model::getPostDetail($id);
        include_once('view/postdetail.php');
        return ;
    }
    public static function textSearch($text) {
        $calendar = Model::getCalendarik();
        $postList = Model::getSearch($text);
        include_once('view/postslist.php');
    }
}//END CLASS
?>















