<style>
.film{
    float: left;
    width: 400px;
    border: 1px solid black;
    box-shadow: 2px 2px 20px rgb(100, 100, 100);
    padding: 20px;
    margin: 20px;
}
.film_description{
    width: 200px;
    float: left;

}
.film_description p{
    margin: 6;
}
.actors_div{
    margin-top: -70;
    float: left;
    height: 200px;
    border: 1px solid black;
    overflow: auto;
}
</style>

<?php

include_once 'movies.php';

$text = "";

foreach ($movies as $movie_name => $info){
    $text.='<div class="film">';
    $text.='<h2> Film: '.$movie_name.'</h2>';
    $text.='<img src="Images/film/'.$info['photo'].'" style="float: left; width: 200px;">';
    $text.='<div class="film_description">';
    $text.='<p> Director: '.$info['director'].'</p>';
    $text.='<p> Year: '.$info['year'].'</p>';
    $text.='<p> Country: '.$info['country'].'</p>';
    $text.='<p> Description: '.$info['description'].'</p>';
    $text.='</div>';
    $text.='<h3 style="float: left; margin-top: -100;"> Actors: </h3>';
    $text.='<div class="actors_div">';
    foreach ($info['actors'] as $actor){
        $text.='<img src="Images/actors/'.$actor['photo'].'" style="float: left; width: 150px;">';
        $text.='<p>'.$actor['name'].'</p>';
    }
    $text.='</div>';
    $text.='</div>';
}

echo $text;
?>
<footer><p>Created by Kezerev JKTV22 2022</p></footer>