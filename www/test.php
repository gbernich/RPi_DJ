<?php
	$mySong = $_GET["song"];
	$myArtist = $_GET["artist"];

	$dbcnx = mysql_connect("localhost", "root", "6314876510");
	$result = mysql_query("USE jukebox");

	$result = mysql_query("SELECT id FROM directory WHERE song='$mySong' AND artist='$myArtist'");
	$id = mysql_fetch_row($result);

	mysql_query("UPDATE queue set voteCount=voteCount+1 WHERE songIndex=" . $id["id"]);
	mysql_query("UPDATE directory set voteCount=voteCount+1 WHERE id=" . $id["id"]);

	// $result = mysql_query("SELECT voteCount FROM queue WHERE songIndex=" . $id["id"]);
 // 	$result = mysql_fetch_row($result);

	 	
?>