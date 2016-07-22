# Lyricaly - Get lyrics direct to your terminal
# By: vigzmv
# www.vigneshm.com
# https://github.com/vigzmv

# Start

# -*- coding: utf-8 -*-

from __future__ import print_function

from bs4 import BeautifulSoup

import requests
import re
import time

while True:

	print()
	print("What are you listening to ?\n")
	songName = raw_input("")

	songName = songName.replace(" ","%20")

	print()
	print(" Fetching the song...")
	print('\n')

	# Lyrics Database: MusixMatch
	# MusixMatch claims itself to be the largerst database of lyrics.
	# Their search is very effective as they automaticaly choose the best match by
	#  parameters like recent trends and popularity. Hence the lyrics can be found with 
	#  least keywords.


	# Searching for the song
	url1 = "https://www.musixmatch.com/search/" + songName

	try:
		respons1 = requests.get(url1)
		soup1 = BeautifulSoup(respons1.content,'html.parser')

	except:

		print(" Please Check Your Internet Connection and try again.")
		continue


	# Get the Best Search result.
	try:
		# bestresult appears first at top in a box
		BestResult = soup1.find_all("div",{"class":"box-style-plain"})

		# get the song lyrics page link
		Link = BestResult[0].find_all("a")[0].get("href")

	except:

		print(" Search Failed! Please check the song name and Retry.")
		continue

	# got the song link
	LyricUrl = "https://www.musixmatch.com" + Link


	# print(LyricUrl)

	# open the lyrics page

	try:

		respons2 = requests.get(LyricUrl)
		soup2 = BeautifulSoup(respons2.content,'html.parser')

	except:

		print(" Please Check Your Internet Connection and try again.")
		continue

	# get the song name form the title
	FoundSongName = soup2.title.string
	FoundSongName = FoundSongName.replace(" lyrics | Musixmatch","")

	# print the Found song name
	found = " Found: " + FoundSongName
	foundlen = len(found)

	print(found.encode("utf-8"))
	print(" ",end="")
	for _ in range(0,foundlen-1):
		print("_",end="")
	
	print('\n\n')
	time.sleep(2)

	# get the lyrics

	# I found that the complete lyrics are stored in a list in scripts section of the page.
	#  a easy way to access the lyrics is by to find the substring "body" which marks
	# the begining of the string.

	try:
		solongtext = soup2.body.findAll(text=re.compile("body"))[0]

		# Lyrics are suceeded by "body"
		start = '"body":"'

		# lyics are followed by its language details
		end = '","language":"en","languageDescription":"English"'

		# stripping the lyrics from the long string
		longtext = solongtext[solongtext.index(start) + len(start) : solongtext.index(end)]

		# Finally th lyrics are in.

		ThemLovelyLyrics = ("  " + longtext)
		
		# Formating the lyrics to show with newlines and ignoring special chahracters
		for i in range(0,len(ThemLovelyLyrics)):
			if ThemLovelyLyrics[i] == '\\' and ThemLovelyLyrics[i+1] == 'n':
				print("\n  ",end="")
			elif ThemLovelyLyrics[i] == '\\' and ThemLovelyLyrics[i+1] == '"':
				pass
			elif ThemLovelyLyrics[i-1] == '\\' and ThemLovelyLyrics[i] == 'n':
				pass
			else:
				print(ThemLovelyLyrics[i].encode("utf-8"),end='')

		print('\n')
		print(' ',end="")
		for _ in range(0,60):
			print("_",end="")
		print('\n')

	except:			
		
		print(" Sorry, Lyrics are not available.")
		continue

# End