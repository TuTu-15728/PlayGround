#!/usr/bin/env python3

import requests
import calendar
from PIL import Image


url = "http://www.pythonchallenge.com/pc/return/mozart.html"
auth = ('huge', 'file')
res = requests.get(url, auth=auth)

print(res.text)
print('+'*50)


img = Image.open('mozart.gif')
width, height = img.size

newImg = Image.new('RGB', size=(640, 480))


first = []
second = []

num = 0
j = 0


for y in range(height):
    for x in range(width):

        if (img.getpixel((x, y)) == 195) and len(first) == 0:
            first.append((img.getpixel((x, y))))

        if (len(first) != 0):
            first.append((img.getpixel((x, y))))

        else:
            second.append((img.getpixel((x, y))))

    fin = first + second

    for i in range(len(fin)-1):
        newImg.putpixel((i, j), fin[i])

    j += 1
    
    first = []
    second = []


newImg.show()
newImg.close()
img.close()
    

