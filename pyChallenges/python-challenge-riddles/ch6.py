#!/usr/bin/env python3

import requests
import re
import zipfile

url = "http://www.pythonchallenge.com/pc/def/channel.html"
res = requests.get(url)

# print(res.text)
print("+"*50)

# The link to download challenge file -- 
# "http://www.pythonchallenge.com/pc/def/channel.zip"


# Starts from here 


# clooecting comments from a zip file

file = zipfile.ZipFile('channel.zip')
infolist = file.infolist()


toCall = "90052"


while (toCall != ""):
	
	with open("channel/"+toCall+".txt", 'r') as f:
		content = f.read()

		for info in infolist:
			if (info.filename) == (toCall + ".txt"):
				print((info.comment).decode('UTF-8'), end='')
		
		if "Next nothing is" in content:
			nextNum = (re.findall(r'Next nothing is (.*)', content, re.DOTALL)[0])
			toCall = nextNum
			# print(content)
		else:
			# print(content)
			break







