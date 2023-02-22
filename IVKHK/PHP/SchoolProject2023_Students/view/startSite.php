<?php
    ob_start();
?>
<h2>Hotels in Estonia</h2>
<div class="main">
    <article>
        <p></p>
        <p></p>
        <p></p>
    </article>
</div>

<?php
    $content=ob_get_clean();
    include 'view/templates/layout.php';
?>