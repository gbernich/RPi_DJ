<!-- <!DOCTYPE html> -->
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <title>RPi JukeBox</title>
  
  <link rel="stylesheet" href="https://d10ajoocuyu32n.cloudfront.net/mobile/1.3.1/jquery.mobile-1.3.1.min.css">
  <link rel="stylesheet" href="queue.css">

  <script src="https://d10ajoocuyu32n.cloudfront.net/jquery-1.9.1.min.js"></script>
  <script src="https://d10ajoocuyu32n.cloudfront.net/mobile/1.3.1/jquery.mobile-1.3.1.min.js"></script>
  <script src="queue.js" type="text/javascript"></script>
</head>

<body>
<!-- Home -->
<div data-role="page" id="page1">
    <div data-theme="a" data-role="header">
        <h5>
            RPi JukeBox
        </h5>
    </div>
    <div data-role="content">
      <!-- <ul data-role="listview" data-divider-theme="b" data-inset="true" class="priorityQ"> -->
        <!-- load queue from SQL database -->
        <?php
          $mySong = $_GET["song"];
          $myArtist = $_GET["artist"];

          $dbcnx = mysql_connect("localhost", "root", "6314876510");
          $result = mysql_query("USE jukebox");
          if($mySong == ".2249"){
            #empty queue command
            mysql_query("DELETE FROM queue");

          }else{
            $result = mysql_query("SELECT * FROM directory WHERE song LIKE '%$mySong%' AND artist LIKE '%$myArtist%' ORDER BY voteCount DESC"); #queries the DB for the search, not sure about the ORDER BY
            
            if(mysql_num_rows($result) == 0){
              echo("<p style=\"text-align:center;\">No Results</p>");
              echo("<div class=\"downloadButton\" style=\"text-align:center;\"><a href=\"\">Download song</a></div>");

            }else{
              echo("<div style=\"text-align:center;\"><p>Song not listed? <a class=\"downloadButton\" href=\"\">Download it!</a></div>");
              echo("<div class=\"homeButton\" style=\"text-align:center;\"><a href=\"\">Go Home</a></div>");
              echo("<ul data-role=\"listview\" data-divider-theme=\"b\" data-inset=\"true\" class=\"priorityQ\">");

              while ( $row = mysql_fetch_array($result) ) { #loops through the rows that were returned
                #builds HTML list
                echo("<li class=\"resultItem\"><table><tr><td class=\"song\"><h6>" . $row["song"] . "</h6></td>  <td class=\"vote\">" . $row["playCount"] . 
                  "</td></tr> <tr><td class=\"artist\">" . $row["artist"] . "</td>  <td class=\"vote\">plays</td></tr></table></li>");
              }
              echo("</ul>");
            }
          }
        ?>
      <!-- </ul> -->
    <div class="homeButton" style="text-align:center;">
        <a href="">Go Home</a>
    </div>
</body>
</html>