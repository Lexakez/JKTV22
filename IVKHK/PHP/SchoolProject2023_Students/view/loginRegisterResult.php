<?php
ob_start();
?>
<div class="container mt-5 text-center">
    <?php
    //vyvod otscheta o vhode
    if (isset($resultLogIn) && $resultLogIn == true) {
        echo '<h3 style="color:green;">Login succeeded. Hello, ' .$_SESSION['name'] . '!</h3>';
    } elseif (isset($resultLogIn) && $resultLogIn == false) {
        echo '<h3 style="color:red;">Login errors</h3><hr>';
        echo '<p><a href="login">Login</a> || <a href="register">Register</a></p>';
    }
    ?>
    <?php
    // вывод отчета о регистрации
    if (isset($resultReg) && $resultReg[0] == true) {
        echo '<h3 style="color:green;">Регистрация успешна, выполните Login</h3>';
        echo '<p><a href="login">Login</a></p>';
    } elseif (isset($resultReg) && $resultReg[0] == false) {
        echo '<h3 style="color:red;">Error!!!!! ' .$resultReg[1] . '</h3>';
        echo '<p><a href="register">Register</a></p>';
    }
    ?>
    <?php
    if (isset($resultChange) && $resultChange[0] == true) {
        echo '<h3 style ="color:green;">Password changed</h3>';
    } elseif (isset($resultChange) && $resultChange[0] == false) {
        echo '<h3 style="color:red;"> No insert change password</h3>';
            echo '<p>'.$resultChange[1].'</p>';
        echo '<p><a href="profile">Go back</a></p>';
    }
    ?>

</div>
<?php
$content = ob_get_clean();
include "view/templates/layout.php";
?>