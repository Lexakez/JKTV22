<?php
class controllerUser
{
    public static function loginForm()
    {
        include_once('view/login.php');
    }
    public static function loginResult()
    {
        $resultLogIn = modelUser::userLogin();
        include_once('view/loginRegisterResult.php');
    }
    public static function logoutAction()
    {
        modelUser::userLogout();
        header('Location:./');
    }
    public static function registerForm()
    {
        include_once('view/register.php');
    }
    public static function registerResult()
    {
        $resultReg = modelUser::userRegister();
        include_once('view/loginRegisterResult.php');
    }
    public static function profileForm()
    {
        include_once('view/profileTable.php');
    }
    public static function profileResult()
    {
        $resultChange = modelUser::userChange();
        include_once('view/loginRegisterResult.php');
    }
}