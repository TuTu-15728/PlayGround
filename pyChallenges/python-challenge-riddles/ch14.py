#!/usr/bin/env python3

from PIL import Image


# url = "http://www.pythonchallenge.com/pc/return/italy.html"

def spiral(x, y):

	newImg = Image.new('RGB', size=(100, 100))

	
	wire =  Image.open('wire.png')
	width, height = wire.size
	p = 0


	top, bottom, left, right = 0, x-1, 0, y-1

	while top <= bottom and left <= right:
				

		for i in range(left, right+1):
			newImg.putpixel((top, i), (wire.getpixel((p, 0))))
			p += 1
			# print(top, i)
		top += 1


		for i in range(top, bottom+1):
			newImg.putpixel((i, right), (wire.getpixel((p, 0))))
			p += 1
			# print(i, right)
		right -= 1

		if top <= bottom:
			for i in range(right, left-1, -1):
				newImg.putpixel((bottom, i), (wire.getpixel((p, 0))))
				p += 1
				# print(bottom, i)
			bottom -= 1

		if left <= right:
			for i in range(bottom, top-1, -1):
				newImg.putpixel((i, left), (wire.getpixel((p, 0))))
				p += 1
				# print(i, left)
			left += 1

	newImg.show()
	newImg.close()
	wire.close()

spiral(100,100)




































# def spiral(x, y):

# 	top, bottom, left, right = 0, x-1, 0, y-1

# 	while top <= bottom and left <= right:

# 		for i in range(left, right+1):
# 			print(top, i)
# 		top += 1

# 		for i in range(top, bottom+1):
# 			print(i, right)
# 		right -= 1

# 		if top <= bottom:
# 			for i in range(right, left-1, -1):
# 				print(bottom, i)
# 			bottom -= 1

# 		if left <= right:
# 			for i in range(bottom, top-1, -1):
# 				print(i, left)
# 			left += 1

# spiral(10, 10)



