#!/usr/bin/env python3

import requests
from PIL import Image


url = "http://www.pythonchallenge.com/pc/return/evil.html"
auth = ('huge', 'file')
res = requests.get(url, auth=auth)

print(res.text)
print('+'*50)


# Working with gfx file

gfx = open('evil2.gfx', 'rb').read()


num = 5
images = {}

for i in range(num):
	images[i] = open('evil/'+str(i)+'.jpg', 'wb')
	images[i].write(bytes(gfx[i :: num]))

for i in range(num):
	images[i].close()


# The Clue for the next Level
# Download evil4 Image file that contains error but Clue

# img_url = "http://www.pythonchallenge.com/pc/return/evil4.jpg"

# res_2 = requests.get(img_url, auth=auth)

# with open('evil4.jpg', 'wb') as evil4:
# 	evil4.write(res_2.content)

# img = open('evil4.jpg', 'rb')
# print(img.read())
# img.close()


