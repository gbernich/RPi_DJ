#!/usr/bin/python
import MySQLdb
import os, sys
import time

try:
	flag = sys.argv[1]
	flag = flag[2:]
	if not flag in ['song', 'artist', 'album', 'filePath', 'voteCount']:
		print "error"
		sys.exit()
except:
	print "error"
	sys.exit()


print flag

#get filename
date = time.strftime("%m_%d_%Y")
fileName = "./log/" + flag + "_" + date + ".txt"
print fileName

#check for directory
if not os.path.exists("./log"):
	os.mkdir("./log")

#open file
myFile = open(fileName, "w")

#connect to database
db = MySQLdb.connect("localhost","root","6314876510")
cursor = db.cursor()
cursor.execute("USE jukebox")
cursor.execute("SELECT song,artist,album,filePath,voteCount FROM directory ORDER BY "+ flag +" DESC")
data = cursor.fetchall()
db.close()

#write data
for row in data:
	myFile.write("%25s | %25s | %25s | %25s | %6d\n" % (str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4])) )
