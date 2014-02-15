<?php
  //check for song request
  $mySong = $_GET["song"];
  $myArtist = $_GET["artist"];

  $dbcnx = mysql_connect("localhost", "root", "6314876510");
  $result = mysql_query("USE jukebox");

  $result = mysql_query("SELECT * FROM directory WHERE song LIKE '%$mySong%' AND artist LIKE '%$myArtist%'");

  if($row = mysql_fetch_array($result)){
    #see if the queue already contains the song
    $check = mysql_query("SELECT * FROM queue WHERE songIndex=" . $row["id"]);

    if(mysql_num_rows($check) == 0){ #doesnt contain song, so add it
      mysql_query("INSERT INTO queue (songIndex, voteCount) VALUES (" . $row["id"] . ", 1)"); //add the songs ID to the queue
      mysql_query("UPDATE directory set voteCount=voteCount+1 WHERE id=" . $row["id"]); //update the voteCount in the directory

    }else{ #contains song so just vote for it
      mysql_query("UPDATE queue set voteCount=voteCount+1 WHERE songIndex=" . $row["id"]); //update the voteCount in the queue
      mysql_query("UPDATE directory set voteCount=voteCount+1 WHERE id=" . $row["id"]); //update the voteCount in the directory 
    }

  }
  //bring back to home page
  header('Location: http://192.168.1.215/');
?>