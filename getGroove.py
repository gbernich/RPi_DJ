from __future__ import print_function
from grooveshark import Client
import sys

client = Client()
client.init()

for song in client.search("dark horse katy perry", type='Songs'):
	print(song.name, song.artist, song.album, sep='-',file=sys.stdout)
	break