<html>
<head>
	<title>Create</title>
</head>
<body>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">

	<label for="deck_title">Deck Title:</label>
	<input type="text" name="deck_title" /><br />
	<label for="number_cards">Number of cards:</label>
	<input type="text" name="number_cards" maxlength=2 /><br />
	<input type="submit" value="Next Page" />

</form>


</body>
</html>
