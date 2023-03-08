<?php
    ob_start();
?>

<h2 class="text-center m-4">Profile data</h2>

    <div class="container text-center" style="width: 450px;">
        <?php
            $profileName=$_SESSION['name'];
            $profileEmail=$_SESSION['email'];

            echo '<h1>Name: '.$profileName.'</h1>';
            echo '<h1>E-mail: '.$profileEmail.'</h1>';
            echo '<h1>Password: ******</h1><hr>';
            echo '<h1>Change Password</h1>';
        ?>
            <form accept-charset="UTF-8" action="profileResult" method="POST" role="form">
            <fieldset>
                <label class="text">Current Password</label>
                <input type="password" name="oldpassword" class="form-control" required />
                <label class="text">New Password</label>
                <input type="password" name="password" class="form-control" required />
                <label class="text">Password Confirm</label>
                <input type="password" name="passwordconfirm" class="form-control" required />
                <a role="button" class="btn btn-primary" href="./">Close</a>
                <button type="submit" class="btn btn-primary" name="send">Save</button>
            </fieldset>
            </form>
    </div>

<?php
    $content = ob_get_clean();
    include "view/templates/layout.php";
?>