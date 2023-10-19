<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

$conn = new mysqli("localhost","root","","worldAngular");
$result = $conn->query("SELECT * FROM city");
$outpworld ="";
$outp = "";
    while($rs = $result->fetch_array(MYSQLI_ASSOC)){
        if($outp !="") {$outp .=",";}
        $outp .= '{"ID":"'.$rs["ID"] .'",';
        $outp .= '"Name":"'.$rs["Name"] .'",';
        $outp .= '"CountryCode":"'.$rs["CountryCode"] .'",';
        $outp .= '"Population":"'.$rs["Population"] .'",';
        $outp .= '}';
    }
$outpworld = '{"records":['.$outp.']}';
$conn->close();
echo($outpworld);
?>