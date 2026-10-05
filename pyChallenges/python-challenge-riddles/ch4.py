#!/usr/bin/env python3

import requests
import re


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
res = requests.get(url)

print(res.text)
print ("+"*70)



url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

i = 0
tocall = "12345"

while i < 400:
	
	res1 = requests.get(url1+tocall)

	if "next nothing" in res1.text:
		print(res1.text)
		nextnothing = re.findall(r'and the next nothing is (.*)', res1.text, re.DOTALL)[0]
		tocall = nextnothing

	elif 'Divide by two' in res1.text:
		print(res1.text)
		tocall = str(int(tocall) // 2)

	else:
		print("Check this out --> ", res1.text)
		break

	i+=1







