#!/usr/bin/env python3

import requests
from PIL import Image


url = "http://www.pythonchallenge.com/pc/return/5808.html"
auth = ('huge', 'file')
res = requests.get(url, auth=auth)


print(res.text)
print("+"*66)


with Image.open('cave.jpg') as cave:
	x, y = cave.size
	
	even = Image.new(size=[640,480], mode='RGB')
	odd = Image.new(size=[640,480], mode='RGB')

	for i in range(x):
		for j in range(y):
			if (i % 2 == 0) and (j % 2 == 0):
				even.putpixel((i,j),(cave.getpixel((i,j))))
			else:
				odd.putpixel((i,j),(cave.getpixel((i,j))))

even.show()
even.close()

odd.show()
odd.close()