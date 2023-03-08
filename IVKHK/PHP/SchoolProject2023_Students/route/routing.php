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
elseif ($route == 'blog') {
	Controller::PostList();
}
elseif ($route == 'posts' && isset($_GET['id']) ) {
	controller::PostDetail($_GET['id']);
}
elseif ($route == 'cal' && isset($_GET['id'])) {
	Controller::Calendar($_GET['id']);
}
elseif ($route == 'search') {
	if (isset($_GET['text'])) {
		Controller::textSearch($_GET['text']);
	} else {
		Controller::error404();
	}
}
elseif ($route == 'login') {
	controllerUser::loginForm();
}
elseif ($route == 'loginResult'){
	controllerUser::loginResult();
}
elseif ($route == 'logout'){
	controllerUser::logoutAction();
}
elseif ($route == 'register') {
	controllerUser::registerForm();
}
elseif ($route == 'registerResult'){
	controllerUser::registerResult();
}
elseif ($route == 'profile') {
	controllerUser::profileForm();
}
elseif ($route == 'profileResult') {
	controllerUser::profileResult();
}
elseif ($route == 'addstudent'){
	controllerStudent::addStudentForm();
}
elseif ($route == 'addstudentResult'){
	controllerStudent::addStudentResult();
}
elseif ($route == 'result'){
	controllerStudent::viewResult();
}
elseif ($route == 'editstudent' && isset($_GET['id'])) {
	controllerStudent::editStudentForm($_GET['id']);
}
elseif ($route == 'editstudentResult' && isset($_GET['id'])) {
	controllerStudent::editStudentResult($_GET['id']);
}
elseif ($route == 'deletestudent' && isset($_GET['id'])) {
	controllerStudent::deleteStudentForm($_GET['id']);
}
elseif ($route == 'deletestudentResult' && isset($_GET['id'])) {
	controllerStudent::deleteStudentResult($_GET['id']);
}
elseif ($route == 'deletestudent' && isset($_GET['id'])) {
	controllerStudent::deleteStudentForm($_GET['id']);
}
elseif ($route == 'deletestudentResult' && isset($_GET['id'])) {
	controllerStudent::deleteStudentResult($_GET['id']);
}
else{
	Controller::error404();
}
