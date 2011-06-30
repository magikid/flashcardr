<?php
class Model{

	public function __construct()
	{
		$db_config = parse_ini_file("model/db.config");
		$user = $db_config['user'];
		$passwd = $db_config['password'];
		$host = $db_config['host'];
		$dbname = $db_config['database_title'];

		try
		{
			$db = new PDO('mysql:host='.$host.';dbname='.$dbname, $user, $passwd);
		}catch (PDOException $e) {
			print "Database error: " . $e->getMessage() . "<br />";
			die();
		}
	}

	public function __destruct()
	{
		$db = null;
	}

	public function getDecksOwned()
	{

		return array(
			"Deckie" => "17",
			"My Deck" => "18"
		);

	}

	public function getCards
	{

	}
?>
