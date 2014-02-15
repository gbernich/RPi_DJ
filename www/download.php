<?php
	$song = $_GET["song"];
	$artist = $_GET["artist"];

	$dbcnx = mysql_connect("localhost", "root", "6314876510");
	$result = mysql_query("USE jukebox");
	//if($result){
	mysql_query("INSERT INTO downloads (song, artist) VALUES (".$song.",".$artist")"); //add the search query to the downloads database
// 		echo("<html><body><p>Hello</p></body></html");
// 	}else{
// 		//bring back to home page
//   		header('Location: http://192.168.1.215/')
//   	}
// ?>