<?php
    ob_start()
?>
<h2>404 ошибка</h2>
<article>
    <h3>404 ошибка - страница не найдена</h3>
</article>

<?php
    $content = ob_get_clean();
    include "view/templates/layout.php";
    