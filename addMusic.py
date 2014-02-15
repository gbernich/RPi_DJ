#!/usr/bin/python
import id3reader
import MySQLdb
import os, sys
import shutil

def getInfo(filePath):
	temp = {}
	id3r = id3reader.Reader(filePath)
	temp['album'] = id3r.getValue('album')
	temp['artist'] = id3r.getValue('performer')
	temp['song'] = id3r.getValue('title')
	return temp


#___MAIN___
drivePath = "/media/JUKEBOX/"
jukeboxPath = "/media/JUKEBOX/jukebox"
mp3Path = drivePath + "/mp3"
m4aPath = drivePath + "/m4a"
convertedPath = drivePath + "/m4a_mp3"
newDir = drivePath + sys.argv[1]
mp3List = []
m4aList = []


#connect to database
db = MySQLdb.connect("localhost", "root", "6314876510")
cursor = db.cursor()
cursor.execute("USE jukebox")
count = 0
#loop through new songs in newDir
for root, dirs, files in os.walk(newDir):
	for song in files:
		songPath = root + "/" + song
		print song
		#ignore m4a files
		temp = song.split('.')
		if len(temp) > 1 and temp[1] != 'm4a':

			#read the file's song info
			info = getInfo(songPath)
			print info
		count += 1

			#check to see if the song already exists in the directory (and database)
			# cursor.execute("SELECT * FROM directory WHERE song=\'"+ song.encode('utf8') + "\' AND artist=\'" + artist.encode('utf8') + "\'")
			# data = cursor.fetchone()
			# print data

			#if it doesnt, check to see if the folder (artist) exists
			#if not data:

				#if it doesnt, create the directory

				#add the file to the directory and database
print count