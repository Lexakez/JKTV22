<style>
.content{
    float: left;
    width: 200px;
}
.clear{
    clear: both;
}

</style>
<?php

include_once 'groups.php';
$text = "";
foreach ($school as $group_name => $info){
    $text.='<h3> Group:'.$group_name.'</h3>';
    $text.='<p><b> Teacher: </b>'.$info['classroomTeacher'].'</p>';
    $text.='<h3> Students list</h3>';
   
    foreach ($info['students'] as $student) {
        $text.='<div class="content">';
        $text.='<p>'.$student['name'].'</p>';
        $text.='<img src="image/'.$student['photo'].'">';
        $text.='</div>';
    }
    
    $text.='<div class="clear"></div><hr>';
}

echo $text;
?>
<p style="margin-top: 20px;"> Design 2021 JKTV22 </p>