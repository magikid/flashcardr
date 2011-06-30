<?php

// index
include_once("controller/Controller.php");

$controller = new Controller($user);
$controller->go();

?>
