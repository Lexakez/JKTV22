<?php
class modelUser
{
    public static function userLogin()
    {
        if (isset($_SESSION['sessionId'])) {
            $result = true;
        } else { 
            $result = false;
            $_SESSION['error'] = 'Неверное имя пользователя или пароль';
            if (isset($_POST['login'])) {
               if (isset($_POST['email']) && isset($_POST['password']) && $_POST['email'] != "" && $_POST['password'] != "") {
                    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
                    $password = filter_input(INPUT_POST, 'password');
                    $sql = "SELECT * FROM users WHERE email = '".$email."'";
                    $database = new database();
                    $item = $database->getOne($sql);

                    if ($item != null) {
                        $password = $_POST['password'];
                        if ($email == $item['email'] && password_verify($password, $item['password'])) { //создаем переменные сессии
                            $_SESSION['sessionId'] = session_id();
                            $_SESSION['userId'] = $item['id'];
                            $_SESSION['name'] = $item['username'];
                            $_SESSION['role'] = $item['role'];
                            $_SESSION['email'] = $item['email'];
                            $result = true;
                        }
                    }
               }
            }
        }
        return $result;
    }

    public static function userLogout()
    {
        session_destroy();
        unset($_SESSION['sessionId']);
        unset($_SESSION['userId']);
        unset($_SESSION['name']);
        unset($_SESSION['role']);
        unset($_SESSION['email']);
    }
    public static function userRegister()
    {
        $result = array(false, 'error register user');
        if (isset($_POST['send'])) {
            $errorString = '';
            $name = $_POST['name'];
            $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
            $password = $_POST['password'];
            $confirm = $_POST['passwordconfirm'];
            if (!$email) {
                $errorString .= "Неправильный email<br />";
            }
            if (!$password || !$confirm || mb_strlen($password) < 6) {
                $errorString .= "Пароль должен быть больше 6 символов <br />";
            }
            if ($password != $confirm) {
                $errorString .= "Пароли не совпадают <vr />";
            }
            if ($errorString == '') {
                $passwordHash = password_hash($_POST['password'], PASSWORD_DEFAULT);
                $sql = "INSERT INTO `users` (`id`, `email`, `password`, `username`) VALUES (NULL, '$email', '$passwordHash', '$name')";
                $database = new database();
                $item = $database->executeRun($sql);
                if ($item){
                    $result = array(true);
                }
                else {
                    $result = array(false, 'Ваш емайл уже зарегистрирован'); //
                }
            } else {
                $result = array(false, $errorString);
            }
        }
        return $result;
    }
    public static function userChange()
   {
    $result = array(false);
    if (isset($_POST['send'])) {
    if (isset($_POST['oldpassword']) && isset($_POST['password']) && isset($_POST['passwordconfirm']) && $_POST['passwordconfirm'] != "" && $_POST['password'] != "") {
        $password= filter_input(INPUT_POST, 'password');
        $oldpassword= filter_input(INPUT_POST, 'oldpassword');
        $confirm= filter_input(INPUT_POST, 'passwordconfirm');
        $sql = "SELECT * FROM `users` WHERE `email` = '". $_SESSION['email'] . "'";
        $database= new database();
        $item = $database->getOne($sql);
        $errorString = '';
        if (password_verify($oldpassword, $item['password']) == false) {
            $errorString .= "Текущий пароль неверен<br />";
        }
        if (!$password || !$confirm || mb_strlen($password) < 6){
            $errorString .= "Пароль должен быть больше 6 символов <br />";
        }
        if ($password != $confirm) {
            $errorString .= "Пароли не совпадают<br />";
        } 
        if ($errorString == ''){
            $result=true;
            $passwordHash= password_hash($_POST['password'], PASSWORD_DEFAULT);
            $sql = "UPDATE `users` SET `password` = '".$passwordHash."' WHERE `users`.`email` = '".$_SESSION['email']."'";
            $database = new database();
            $item = $database->executeRun($sql);
            if ($item != null){
                $result = array(true);
            } else {
                $result = array(false,'Упсс, не обновился пароль');
            }
            
        }
        else {
            $result = array(false, $errorString);
        }
    }
    }
    return $result;
   }
}