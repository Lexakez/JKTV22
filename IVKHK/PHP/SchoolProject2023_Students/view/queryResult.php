<?php
ob_start();
?>
<div class="container text-center" style="width:80%; ">

    <?php
    if (isset($_SESSION['result'])) {
        if ($_SESSION['result'] == true) {
    ?>
            <div class="alert alert-info">
                <strong>Запрос успешно выполнен</strong>
            </div>
        <?php
        } else if ($_SESSION['result'] == false) {
        ?>
            <div class="alert alert-warning">
                <strong>Ошибка выполнения запроса!</strong>
            </div>
    <?php
        }
        unset($_SESSION['result']);
    }
    ?>
  
</div>

<?php
$content = ob_get_clean();
include "view/templates/layout.php";
?>