from __future__ import print_function
from grooveshark import Client
import sys

userIn = sys.argv[1]

client = Client()
client.init()

for song in client.search(userIn, type='Songs'):
	print(song.name, song.artist, sep=';')
	break