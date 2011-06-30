<html>
<head>
	<title>Edit</title>
</head>
<body>
	<h2><?php $deck->title; ?></h2>
	<table>
	<th>#</th><th>Front</th><th>Back</th>
	<?php

		foreach ($cards as $card)
		{
			echo '<tr><td>'.$card->number.'</td><td>'.$card->front.'</td><td>'.$card->back.'</td></tr>';

	?>
</body>
</html>
