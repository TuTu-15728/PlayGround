#!/usr/bin/env python3

import requests
import re


url = "http://www.pythonchallenge.com/pc/def/equality.html"
res = requests.get(url)


patt = r'<!--(.*?)-->'
data = re.findall(patt, res.text, re.DOTALL)[0]
# print(data)


myStr = ""

for i in range(len(data)):
	if data[i].islower():
		if data[i-1].isupper() and data[i-2].isupper() and data[i-3].isupper():
			if data[i+1].isupper() and data[i+2].isupper() and data[i+3].isupper():
				if data[i-4].islower() and data[i+4].islower():
					myStr += data[i]



print(myStr)


newurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php"