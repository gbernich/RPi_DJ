<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="20">
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <title></title>
  
  <link rel="stylesheet" href="https://d10ajoocuyu32n.cloudfront.net/mobile/1.3.1/jquery.mobile-1.3.1.min.css">
  
  <!-- Extra Codiqa features -->
  <link rel="stylesheet" href="queue.css">
  
  <!-- jQuery and jQuery Mobile -->
  <script src="https://d10ajoocuyu32n.cloudfront.net/jquery-1.9.1.min.js"></script>
  <script src="https://d10ajoocuyu32n.cloudfront.net/mobile/1.3.1/jquery.mobile-1.3.1.min.js"></script>

  <!-- Extra Codiqa features -->
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

        <div data-role="fieldcontain" class="requestBox">
          <form action="#" onsubmit="return false;">
            <input name="" id="textinput1" class="requestInput" placeholder="&lt; song - artist &gt;" value=""
            type="text" value="Search">
          </form>
        </div>

        <ul data-role="listview" data-divider-theme="b" data-inset="true" class="priorityQ">
          <!-- load queue from SQL database -->
          <?php
            $dbcnx = mysql_connect("localhost", "root", "6314876510");
            $result = mysql_query("USE jukebox");
            $result = mysql_query("SELECT songIndex, voteCount FROM queue ORDER BY voteCount DESC");
            while ( $row = mysql_fetch_array($result) ) {
              $match = mysql_query("SELECT song, artist from directory WHERE id=" . $row["songIndex"]);
              $match = mysql_fetch_array($match);
              echo("<li class=\"listItem\"><table><tr><td class=\"song\"><h6>" . $match["song"] . "</h6></td>  <td class=\"vote\"><h6>VOTE</h6>
                </td></tr> <tr><td class=\"artist\">" . $match["artist"] . "</td>  <td class=\"vote\">" . $row["voteCount"] . "</td></tr></table></li>");
            }
          ?>
        </ul>

    </div>
</div>
</body>
</html>
