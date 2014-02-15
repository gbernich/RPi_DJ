#!/usr/bin/python
import id3reader
import os, sys, re
import shutil
import MySQLdb

drivePath = "/media/JUKEBOX/"
jukeboxPath = "/media/JUKEBOX/jukebox"
mp3Path = drivePath + "/mp3"
m4aPath = drivePath + "/m4a"
convertedPath = drivePath + "/m4a_mp3"
musicPath = drivePath + sys.argv[1]
mp3List = []
m4aList = []

def sortMusicFileTypes():
	# get a list of mp3's and a list of m4a's
	for root, dirs, files in os.walk(musicPath):
		for song in files:
			songPath = root + "/" + song
			temp = song.split('.')
			if len(temp) == 2:
				extension = temp[1]
				if extension == 'm4a':
					#rename file
					newPath = root + "/" + temp[0] + '.mp3'
					shutil.move(songPath, newPath)
					print songPath 
					print newPath
					songPath = newPath

			# if extension in ['mp3', 'wav']:
			# 	mp3List.append(songPath)
			
	#move the files to ../mp3
	# if os.path.exists(mp3Path):
	# 	try:	os.system('rm -r ' + mp3Path)
	# 	except:	print "here1"
	# try:	os.mkdir(mp3Path)
	# except:	pass
	# for song in mp3List:
	# 	try:
	# 		shutil.move(song, mp3Path)
	# 	except:
	# 		pass

def convertFiles():
    os.system("python ./ConvertToMP3.py " + m4aPath)

def buildDirAndDB():
	if not os.path.exists(jukeboxPath):
		os.mkdir(jukeboxPath)

	#connect to database
	db = MySQLdb.connect("localhost","root","6314876510")
	cursor = db.cursor()
	cursor.execute("USE jukebox")

	#go thru MP3 files
	reg = re.compile("^[0-2][0-9]\s.*")
	for root, dirs, files in os.walk(musicPath):
		for song in files:
			if song[0] != '.':
				songPath = root + "/" + song
				try:
					info = getInfo(songPath)
				except:
					info = {'song':None, 'artist':None, 'album':None}
				
				#add to jukebox directory
				try:
					artist = info['artist']
					if artist == None:
						artist = root.split('/')
						artist = artist[len(artist)-2]
					artist = ''.join(e for e in artist if (e.isalnum() or e.isspace()))
					artist = artist.strip()

					album = info['album']
					if album == None:
						album = root.split('/')
						album = album[len(album)-1]
					album = ''.join(e for e in album if (e.isalnum() or e.isspace()))
					album = artist.strip()
					
					song2 = info['song']
					if song2 == None:
						#removing leading Track Number
						m = reg.match(song)
						if m: #REMOVE TRACK NUMBER (stupid iTunes)
							songArray = song.split(' ')
							songArray.pop(0)
							song2 = ' '.join(songArray)
						else:
							song2 = song
						song2 = song2.split('.')[0]	
					song2 = ''.join(e for e in song2 if (e.isalnum() or e.isspace()))
					song2 = song2.strip()

					filePath = jukeboxPath + "/" + artist + "/" + song
					#print filePath
					#check DB for song (if it has a name)
					#print song2
					if song2 != None and '.m4a' not in filePath:
						cursor.execute("SELECT * FROM directory WHERE song=\'"+ song2 + "\' AND artist=\'" + artist + "\'")
						data = cursor.fetchone()
						if data == None: #no match found so add song to DB and directory
							print info
							#create folder for artist and add song
							newPath = jukeboxPath + "/" + artist
							if not os.path.exists(newPath):
								os.mkdir(newPath)
							temp = newPath.split('/')
							temp.pop()
							renamed = "/".join(temp)
							newPath = renamed + "/" + artist + "/" + song
							shutil.copyfile(songPath, newPath)

							#add to DB
							cursor.execute("INSERT INTO directory (song, artist, album, filePath, voteCount) VALUES (\'" + song2 + "\', \'" + artist+ "\', \'" + album + "\', \'" + filePath + "\', 0)")
							db.commit()
					else:
						print "already have"

				except:
					print "skipped ", songPath



#returns the id3 info
def getInfo(filePath):
	temp = {}
	id3r = id3reader.Reader(filePath)
	temp['album'] = id3r.getValue('album')
	temp['artist'] = id3r.getValue('performer')
	temp['song'] = id3r.getValue('title')
	return temp

#Adds songs to database from the already-built jukebox directory
def addToDB():
	#connect to database
	db = MySQLdb.connect("localhost","root","6314876510")
	cursor = db.cursor()
	cursor.execute("USE jukebox")

	#go thru jukebox files
	for root, dirs, files in os.walk(jukeboxPath):
		for song in files:
			songPath = root + "/" + song
			info = getInfo(songPath)
			try:	song = info["song"].replace("\'", "")
			except:	song = ""
			try:	artist = info["artist"].replace("\'", "")
			except:	artist = ""
			try:	album = info["album"].replace("\'", "")
			except:	album = ""

			cursor.execute("SELECT * FROM directory WHERE song=\'"+ song.encode('utf8') + "\' AND artist=\'" + artist.encode('utf8') + "\'")
			data = cursor.fetchone()
			if not data:
				try:
					cursor.execute("INSERT INTO directory (song, artist, album, filePath, voteCount) VALUES (\'" + song.encode('utf8') + "\', \'" + artist.encode('utf8') + "\', \'" + album.encode('utf8') + "\', \'" + songPath.encode('string-escape') + "\', 0)")
				except:
					print "ERROR inserting"
			else:
				print "          found"
	db.commit()
	db.close()

#_____MAIN_____
#sortMusicFileTypes()
# convertFiles()
buildDirAndDB()
#addToDB()




