<?php
include_once("model/Model.php");

class Controller {
	public $model;

	public function __construct($user)
	{
		$this->model = new Model($user);
	}

	public function go()
	{
		switch ($_GET['page']){

			case "create":
				if(!isset($_POST['deck_title']))
					include 'view/create_deck.php'
				else
					include 'view/create_cards.php';
				break;

			case "edit":
				if(!isset($_GET['deck_title']))
					include 'view/select_deck.php';
				else
					include 'view/edit_cards.php';

				break;

			case "study":
				if(!isset($_GET['deck_title']))
					include 'view/select_deck.php';
				else
					include 'view/study_cards.php';
				break;
		}
	}

}
?>
