<?php
	$song = $_GET["song"];
	$artist = $_GET["artist"];
	$dbcnx = mysql_connect("localhost", "root", "6314876510");
	if($dbcnx){
		$result = mysql_query("USE jukebox");
		mysql_query("INSERT INTO downloads (song, artist) VALUES ('$song', '$artist')"); //add the search query to the downloads database
		header('Location: http://192.168.1.215/');
	}
?>