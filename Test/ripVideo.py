#!/usr/bin/python
import urllib2, subprocess, os
from bs4 import BeautifulSoup

search = 'katy perry dark horse'
url = 'http://www.youtube.com/results?search_query=' + search.replace(" ", "+")

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

soup = BeautifulSoup(data)
find = soup.find(id="search-results").find('li').find('a')

urlExt = find['href'].strip('/')
url = 'http://www.youtube.com/' + urlExt
fileName = urlExt.split('=')
try:	fileName = fileName[1]
except:	fileName = fileName[0]

#get title of video
cmd = ["youtube-dl", "--get-title", url]
songData = subprocess.check_output(cmd).strip()

#get filename from youtube
cmd = ["youtube-dl", fileName, "-o", "~/Desktop/new/%(title)s.%(ext)s", "--extract-audio", "--audio-format" , "mp3", "--audio-quality", "192K", "--add-metadata"]
subprocess.call(cmd)

# filePath = "/var/www/" + fileName
# print filePath

# #get youtube video
# cmd = ["youtube-dl", "-o", filePath, url]
# out = subprocess.check_output(cmd)

# #video to wav
# wavPath = filePath.split('.')
# wavPath[len(wavPath)-1] = 'wav'
# wavPath = '.'.join(wavPath)
# cmd = ["ffmpeg", "-i", filePath, wavPath]
# out = subprocess.check_output(cmd)
# print os.path.exists(filePath)
# try:	os.remove(filePath) #remove video
# except OSError as e:	print e

# #wav to mp3
# mp3Path = wavPath.split('.')
# mp3Path[len(mp3Path)-1] = 'mp3'
# mp3Path = '.'.join(mp3Path)
# cmd = ["lame", wavPath, mp3Path]
# out = subprocess.check_output(cmd)
# try:	os.remove(wavPath) #remove wav
# except OSError: print e