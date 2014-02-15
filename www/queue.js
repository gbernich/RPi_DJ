var ip = "http://192.168.1.215/"

$(document).ready(function(){

	//ENABLES PRESSING ENTER TO SUBMIT
	$('.requestInput').bind('keypress', function(e) {
		if(e.keyCode == 13){
			e.preventDefault();
			requestResults();
		}
	});
	$('.downloadInput').bind('keypress', function(e) {
		if(e.keyCode == 13){
			e.preventDefault();
			requestDownload();
		}
	});

	//VOTE CLICK
	$('.vote').click(function(i, obj){
		var song = $(this).parents('table:first').find('.song:first').find('h6:first').text();
		var artist = $(this).parents('table:first').find('.artist:first').text();
		window.location.href = ip+"vote.php?song=" + song + "&artist=" + artist;
	});

	//REQUEST SONG CLICK
	$('.resultItem').click(function(i, obj){
		$(this).css("text-color", "green") //turn text green for some user feedback

		//get song and artist
		var song = $(this).find('.song:first').find('h6:first').text();
		var artist = $(this).find('.artist:first').text();

		//load request for selected song
		window.location.href = ip+"request.php?song="+song.replace(/^\s+|\s+$/g, "")+"&artist="+artist.replace(/^\s+|\s+$/g, "");
	});

	//GO HOME TO QUEUE
	$('.homeButton').click(function(i,obj){
		window.location.href = ip;
	});

	//GO TO DOWNLOAD PAGE
	$('.downloadButton').click(function(i,obj){
		window.location.href = ip + "download.html";
	});


});

//LOADS PAGE OF SEARCH RESULTS
function requestResults()
{
	var input = $('.requestInput').val();
	$('.requestInput').val(''); //reset textbox
	var inputArray = input.split('-');

	if(inputArray.length == 1)
	{
		inputArray.push("");
	}

	//loads request
	var song = escape(inputArray[0].trim());
	var artist = escape(inputArray[1].trim());

	window.location.href = ip+"results.php?song="+song.replace(/^\s+|\s+$/g, "")+"&artist="+artist.replace(/^\s+|\s+$/g, "");
}

//LOADS PHP TO REQUEST DOWNLAOD
function requestDownload()
{
	//console.log("here");
	var input = $('.downloadInput').val();
	$('.downloadInput').val(''); //reset textbox
		var inputArray = input.split('-');

	if(inputArray.length == 1)
	{
		inputArray.push("");
	}

	//loads request
	var song = escape(inputArray[0].trim());
	var artist = escape(inputArray[1].trim());

	window.location.href = ip+"dl.php?song="+song.replace(/^\s+|\s+$/g, "")+"&artist="+artist.replace(/^\s+|\s+$/g, "");
}