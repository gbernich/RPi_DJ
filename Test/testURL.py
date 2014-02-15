#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import mechanize

search = 'santeria sublime'
url = 'http://www.youtube.com/results?search_query=' + search.replace(" ", "+")

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

soup = BeautifulSoup(data)

find = soup.find(id="search-results").find('li').find('a')

url = find['href']
url = 'http://www.youtube.com' + url
print url
print "Processing Video..."

br = mechanize.Browser()
# br.open("http://www.audiothief.com/")
br.open("http://www.getvideomp3.com/youtubetomp3/")
br.select_form(nr=0)
print br.form
# br['VideoUrl'] = url
# response = br.submit()
#print response.read()

print "File Downloading..."


print "File Converting..."

# br.submit('http://www.vidtomp3.com/')
# http://www.listentoyoutube.com/

