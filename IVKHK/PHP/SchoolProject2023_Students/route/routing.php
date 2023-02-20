<?php
/*URI унифицированный идентификатор ресурса, 
	который был предоставлен для доступа к странице
знак ? отделяет полный путь и значение 
	переменной идентификатора для фильтрации
*/
//полный путь к проекту до знака ?
$path = explode('?', $_SERVER['REQUEST_URI'])[0];
//количество папок вложений - считаем символы "/"
$num = substr_count($path, '/');
//вычисляем маршрут после последнего символа "/"
$route = explode('/', $path)[$num];
//значение переменной - идентификатора фильтрации - после знака ?
if($route == '' OR $route == 'index.php'){
	Controller::StartSite();
}
elseif ($route == 'students') {
	Controller::StudentList();
}
elseif ($route == 'studByspec' && isset($_GET['id'])){
	Controller::StudentByspec($_GET['id']);
}
elseif ($route == 'student' && isset($_GET['id'])){
	Controller::StudentDetail($_GET['id']);
}
else{
	Controller::error404();
}
