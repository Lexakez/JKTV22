<?php

class Controller {
    public static function startSite(){
        include_once 'view/startSite.php';
    }
    public static function contactView(){
        include_once 'view/contact.php';
    }
    public static function error404(){
        include_once 'view/error404.php';
    }
}