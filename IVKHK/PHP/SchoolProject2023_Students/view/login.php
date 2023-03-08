<?php
ob_start();
?>

<h2 class="text-center m-4">Login</h2>
<div class="container" style="width: 450px">
    <form action="loginResult" method="POST">
        <!-- Email input -->
        <label class="text">Login</label>
        <input type="email" name="email" class="form-control" required />
        <label class="text">Password</label>
        <input type="password" name="password" class="form-control" required />
        <button type="submit" class="btn btn-primary" name="login">Sign in</button>
        
    </form>
</div>
<?php
$content = ob_get_clean();
include "view/templates/layout.php";
?>