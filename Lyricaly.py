from __future__ import print_function

import requests
from bs4 import BeautifulSoup
import re

songName = raw_input()

songName = songName.replace(" ","%20")

url1 = "https://www.musixmatch.com/search/" + songName

respons1 = requests.get(url1)

soup1 = BeautifulSoup(respons1.content,'html.parser')

# print soup1.title.string
# print

BestResult = soup1.find_all("div",{"class":"box-style-plain"})

Link = BestResult[0].find_all("a")[0].get("href")

# print Link
# print

LyricUrl = "https://www.musixmatch.com" + Link


print(LyricUrl)
print

respons2 = requests.get(LyricUrl)

soup2 = BeautifulSoup(respons2.content,'html.parser')

FoundSongName = soup2.title.string
FoundSongName = FoundSongName.replace("| Musixmatch","")

print(FoundSongName)
print

solongtext = soup2.body.findAll(text=re.compile("body"))[0]

start = '"body":"'
end = '","language":"en","languageDescription":"English"'

longtext = solongtext[solongtext.index(start) + len(start) : solongtext.index(end)]

ThemLovelyLyrics = str(longtext)


for i in range(0,len(ThemLovelyLyrics)):
	if ThemLovelyLyrics[i] == '\\' and ThemLovelyLyrics[i+1] == 'n':
		print()
	elif ThemLovelyLyrics[i-1] == '\\' and ThemLovelyLyrics[i] == 'n':
		continue
	else:
		print(ThemLovelyLyrics[i],end='')