#!/usr/bin/env python

# Lyricaly - Get lyrics directly to your terminal
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
import urllib2

def main():

	count = 0
	while True:

		print()

		if count == 0:
			print("What are you listening to ?\n")
		else:
			print("What are you listening to ?  (enter 'exit' to exit)\n")

		songName = raw_input("")

		if songName == 'exit' or songName == 'Exit' or songName == 'EXIT':
			exit()

		songName = songName.replace(" ","%20")

		print("")
		print("Fetching the song...")

		# Lyrics Database: MusixMatch
		# MusixMatch claims itself to be the largerst database of lyrics.
		# Their search is very effective as they automaticaly choose the best match by
		# parameters like recent trends and popularity. Hence the lyrics can be found with
		# least keywords.

		# Earlier Python requests did the job, but some changes in MusixMatch blocked requests from it.
		# Now using urllib2 to fet this done

		# Searching for the song

		url1 = "https://www.musixmatch.com/search/" + songName

		# print(url1)
		try:
			response = urllib2.urlopen(url1)
			# respons1 = requests.get(url1)
			# print(response)
			soup1 = BeautifulSoup(response,'html.parser')

		except:

			print(" \n\nPlease Check Your Internet Connection and try again.\n")
			continue

		# Get the Best Search result.
		try:
			# bestresult appears first at top in a box
			BestResult = soup1.find_all("div",{"class":"box-style-plain"})

			# get the song lyrics page link
			Link = BestResult[0].find_all("a")[0].get("href")

		except:

			print(" \n\nSearch Failed! Please check the song name and Retry.\n")
			continue

		# got the song link
		LyricUrl = "https://www.musixmatch.com" + Link


		# print(LyricUrl)

		# open the lyrics page

		try:

			respons2 = urllib2.urlopen(LyricUrl)
			# respons2 = requests.get(LyricUrl)
			soup2 = BeautifulSoup(respons2,'html.parser')

		except:

			print(" \n\nPlease Check Your Internet Connection and try again.\n")
			continue

		# get the song name form the title

		FoundSongName = soup2.title.string
		FoundSongName = FoundSongName.replace(" lyrics | Musixmatch","")

		# print the Found song name

		found = " Song: " + FoundSongName
		foundlen = len(found)

		print('\n\n')

		print()
		for _ in range(0,70):
			print("-",end="")
		print('\n')
		for _ in range(0,35-(foundlen/2)):
			print(" ",end="")
		print(found.encode("utf-8"))
		print()
		print("",end="")
		for _ in range(0,70):
			print("-",end="")


		print('\n\n')
		time.sleep(1)

		# get the lyrics

		# I found that the complete lyrics are stored in a list in scripts section of the page.
		# a easy way to access the lyrics is by to find the substring "body" which marks
		# the begining of the string.

		try:

			verylongtext = soup2.body.findAll(text=re.compile('"body"'))
			# print(len(verylongtext))
			solongtext = verylongtext[0]

			# Lyrics are suceeded by "body"
			start = '"body":"'

			# lyics are followed by its language details
			end_en = '","language":"en","languageDescription":"English"'
			end_es = '","language":"es","languageDescription":"Spanish"'
			end_fr = '","language":"fr","languageDescription":"French"'
			end_un = '","language":"","languageDescription":""'

			# stripping the lyrics from the long string

			# checking for the lyrics languwage
			if end_en in solongtext:
				# english
				longtext = solongtext[solongtext.index(start) + len(start) : solongtext.index(end_en)]

			elif end_es in solongtext:
				# spanish
				longtext = solongtext[solongtext.index(start) + len(start) : solongtext.index(end_es)]

			elif end_fr in solongtext:
				# french
				longtext = solongtext[solongtext.index(start) + len(start) : solongtext.index(end_fr)]

			elif end_un in solongtext:
				# unknown (hindi)
				longtext = solongtext[solongtext.index(start) + len(start) : solongtext.index(end_un)]

			else:
				print(" Sorry, Lyrics are not available.\n")
				continue

			# Finally the lyrics are in.

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
			print('',end="")
			for _ in range(0,70):
				print("_",end="")
			print('\n\n')
			count = count + 1

		except:

			print(" Sorry, Lyrics are not available.\n")
			continue

if __name__ == "__main__":
    main()
# End
