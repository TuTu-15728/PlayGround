#!/usr/bin/env python3


from PIL import Image

numList = ""

with Image.open("oxygen.png") as img:
	for  i in range(0, img.width - 21, 7):
		value = (img.getpixel((i,47))[0])
		numList += chr(value)

print(numList)

nextLevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]

nextLink = ""

for each in nextLevel:
	nextLink += chr(each)

print(nextLink)

newurl = "http://www.pythonchallenge.com/pc/def/integrity.html"


