<?php
ob_start();
?>

<h2 class="text-center m-4">Register</h2>
<div class="container" style="width: 450px">
    <form action="registerResult" method="POST">
        <!-- Email input -->
        <label class="text">Name</label>
        <input type="name" name="name" class="form-control" required />
        <label class="text">E-mail</label>
        <input type="email" name="email" class="form-control" required />
        <label class="text">Password</label>
        <input type="password" name="password" class="form-control" required />
        <label class="text">Password Confirm</label>
        <input type="password" name="passwordconfirm" class="form-control" required />
        <button type="submit" class="btn btn-primary" name="send">Register</button>
        
    </form>
</div>
<?php
$content = ob_get_clean();
include "view/templates/layout.php";
?>