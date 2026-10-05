#!/usr/bin/env python3

import requests
import gzip
import difflib
import io

# url = "http://www.pythonchallenge.com/pc/return/balloons.html"
# url_2 = "http://www.pythonchallenge.com/pc/return/brightness.html"
# auth = ("huge", "file")

# response = requests.get(url, auth=auth)
# response_2 = requests.get(url_2, auth=auth)

# print(response.text)
# print("+"*50)
# print(response_2.text)
# print("+"*50)

my_file = open('delta.txt')
lines = my_file.readlines()

seq_1 = []
seq_2 = []


for line in lines:
    seq_1.append(line[:55].strip() + '\n')
    seq_2.append(line[55:].strip() + '\n')


    # Try to fix the below code

    # for i in range(len(line)):
    #     if line[i] == ' ' and line[i+1] == ' ':
    #         firstSec = line[:i].strip() + '\n'
    #         seq_1.append(firstSec)
            
    #         secondSec = line[i+3:].strip() + '\n'
    #         seq_2.append(secondSec)


img_1 = open("image_1.png", 'wb')
img_2 = open("image_2.png", 'wb')
both_img = open("both_image.png", 'wb')


differ = difflib.Differ()
comparison = list(differ.compare(seq_1, seq_2))

b = io.BytesIO()

for each in comparison:
    bytes_to_write = bytes([int(b, 16) for b in each[2:].split()])

    if each.startswith('+'):
        img_1.write(bytes_to_write)

    if each.startswith('-'):
        img_2.write(bytes_to_write)

    if each.startswith(' '):
        both_img.write(bytes_to_write)


    # if each.startswith('+'):
    #     data_to_write = each[2:].split()
    #     for items in data_to_write:
            # print(items)
            
        # final_write = [chr (int(every, 16)) for every in data_to_write]


img_1.close()
img_2.close()
both_img.close()