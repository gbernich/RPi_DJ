#!/usr/bin/python
import MySQLdb
import pygame
import time, threading, sys
import urllib2, subprocess, os
from bs4 import BeautifulSoup

def confirmSongAndArtist(search):
	replaceList = ["(Official Music Video)", "[Official Music Video]", "YouTube", "(Official Video)", "[Official Video]"]
	out = subprocess.check_output(["youtube-dl", search, "--get-title"])
	out = out.split('-')
	for x in out:
		x = x.strip()
	out = ' '.join(out)
	out.strip()
	for x in replaceList:
		out = out.replace(x, '')

	groove = subprocess.check_output(["python", "testGroove.py", out])
	groove = groove.strip()
	groove = groove.split(';')
	
	try:
		song = groove[0]
		artist = groove[1]
	except:
		song = ""
		artist = ""
	return song, artist

class playMusic(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		#set up music player
		pygame.mixer.init()
		musicPlayer = pygame.mixer.music
		play = True
		volume = 0.75
		musicPlayer.set_volume(1.0)

		#set up MySQL
		db = MySQLdb.connect("localhost","root","6314876510")

		while(True):
			#get top of queue
			try:
				time.sleep(0.5)
				cursor = db.cursor()
				cursor.execute("USE jukebox")
				cursor.execute("SELECT id,songIndex,voteCount FROM queue ORDER BY voteCount DESC")
				data = cursor.fetchone()
				
				queueID = data[0]
				songIndex = data[1]
				voteCount = data[2]

				#get file path of song
				cursor.execute("SELECT filePath FROM directory WHERE id=%ld" % songIndex)
				data = cursor.fetchone()
				filePath = data[0]
				print filePath

				#play the song
				try:
					musicPlayer.load(filePath)
					musicPlayer.play()
					cursor.execute("DELETE FROM queue WHERE id=%ld" % queueID)
					db.commit()
				except:
					print "Error: Could not play song."
			except:
				print "Empty"

			#wait for song to finish
			while(musicPlayer.get_busy()):
				time.sleep(1.0)
			cursor.close()
		db.close()
	

class downloadMusic(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		#set up MySQL
		db = MySQLdb.connect("localhost","root","6314876510")
		while(True):
			search = "None"
			#get search from database
			try:
				cursor = db.cursor()
				cursor.execute("USE jukebox")
				cursor.execute("SELECT song, artist, id FROM downloads")
				data = cursor.fetchone()
				if not data:
					raise Exception("No songs to download.")
				song = str(data[0].replace("\'", ""))
				artist = str(data[1].replace("\'", ""))
				songID = str(data[2]).replace("\'", "")
				album = "YouTube"

				#search on YouTube
				search = song + " " + artist + " vevo"
				url = 'http://www.youtube.com/results?search_query=' + search.replace(" ", "+")

				usock = urllib2.urlopen(url)
				data = usock.read()
				usock.close()

				soup = BeautifulSoup(data)
				find = soup.find(id="search-results").find('li').find('a')

				urlExt = find['href'].strip('/')
				url = 'http://www.youtube.com/' + urlExt

				#get artist and song name using Grooveshark and YouTube
				search = song + " " + artist
				search = search.strip()
				song, artist = confirmSongAndArtist(search)
				if song == "" or artist == "":
					cursor.execute("DELETE FROM downloads WHERE id="+ songID)
					db.commit()
					raise Exception("Not a valid song, punk.")

				#fileName = urlExt.split('=')
				fileName = song

				#get filename from youtube
				songPath = "/media/JUKEBOX/jukebox/"+artist.title()+"/" +song.title() +".%(ext)s"
				cmd = ["youtube-dl", fileName, "-o", songPath, "--extract-audio", "--audio-format" , "mp3", "--audio-quality", "192K"]
				outcome = subprocess.call(cmd)

				songPath = "/media/JUKEBOX/jukebox/"+artist.title()+"/" +song.title() +".mp3"

				#if exit code is zero, add song to directory and queue
				if outcome == 0:
					cursor.execute("INSERT INTO directory (song, artist, album, filePath, voteCount) VALUES (\'" + song.title() + "\', \'" + artist.title() + "\', \'" + album.encode('utf8') + "\', \'" + songPath.encode('string-escape') + "\', 0)")
					#cursor.execute("DELETE FROM downloads WHERE song=\'" + song + "\' AND artist=\'"+ artist + "\'")
					cursor.execute("DELETE FROM downloads WHERE id=\'"+ songID+"\'")
					cursor.execute("SELECT id FROM directory WHERE song=\'" + song.title() + "\' AND artist=\'"+ artist.title() + "\'")
					newID = cursor.fetchone()[0]
					cursor.execute("INSERT INTO queue (songIndex, voteCount) VALUES (" + str(newID) + ", 1)")
					db.commit()

					#remove m4a file
					try:	os.remove(songPath[:-3] + "m4a")
					except OSError as e:	print e
				else:
					raise Exception("failed")

			except:
				print sys.exc_info()[1]
			cursor.close()
			time.sleep(5)
		db.close()


#MAIN
threads = []

thread = playMusic()
thread.start()
threads.append(thread)

thread = downloadMusic()
thread.start()
threads.append(thread)

for thread in threads:
    thread.join()



