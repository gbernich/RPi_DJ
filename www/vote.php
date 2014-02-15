<?php
  //check for song and artist
  $mySong = $_GET["song"];
  $myArtist = $_GET["artist"];

  $dbcnx = mysql_connect("localhost", "root", "6314876510");
  $result = mysql_query("USE jukebox");

  $result = mysql_query("SELECT id FROM directory WHERE song='$mySong' AND artist='$myArtist'");
  $id = mysql_fetch_array($result);
  mysql_query("UPDATE queue set voteCount=voteCount+1 WHERE songIndex=" . $id["id"]);
  mysql_query("UPDATE directory set voteCount=voteCount+1 WHERE id=" . $id["id"]);

  //bring back to home page
  header('Location: http://192.168.1.215/')
?>