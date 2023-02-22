<?php
/* проверка URL адреса и перенаправление в
 * соответствующую функцию контроллера: 
 * startSite - hotels, error404
 */
 //прочитаем и разделим адрес по символу '?' - до знака ?
$host=explode('?',$_SERVER['REQUEST_URI'])[0];
//посчитаем символы /, т.е. сколько вложений папок от корня сервера
$num= substr_count($host, '/');
//возьмем последний текст после символа -это и есть маршрут
$path=explode('/',$host)[$num];
//---------------------------------
if($path=='' || $path=='index.php'){
    //start page
    Controller::startSite();
}
elseif($path=='contact'){
    Controller::contactView();
}
else{
    Controller::error404();
}











