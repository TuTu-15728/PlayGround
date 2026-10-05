#!/usr/bin/env python3

import requests
import re
import bz2
from urllib.parse import unquote
from urllib.parse import unquote_plus, unquote_to_bytes

from xmlrpc.client import ServerProxy

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
url_2 = "http://www.pythonchallenge.com/pc/stuff/violin.php"
auth = ('huge', 'file')
headers = { "Cookie": "info=the flowers are on their way"}

i = 0
firstCall = "12345"

data = ""


# while i < 400:
	
# 	res1 = requests.get(url+firstCall)
# 	cookies = res1.cookies

# 	data += (cookies['info'])

# 	if "next busynothing" in res1.text:
# 		print(res1.text)
# 		nextnothing = re.findall(r'the next busynothing is (.*)', res1.text, re.DOTALL)[0]
# 		firstCall = nextnothing

# 	elif 'Divide by two' in res1.text:
# 		print(res1.text)
# 		firstCall = str(int(firstCall) // 2)

# 	else:
# 		print("Check this out --> ", res1.text)
# 		break

# 	i+=1


# res = unquote_to_bytes(data.replace("+", " "))

# print(bz2.decompress(res).decode())
# print('+'*50)



# Cause an ERROR but the output is '555-VIOLIN'

# conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# print(conn.phone("Leopold"))



response = requests.get(url_2, auth=auth, headers=headers)

print(response.text)
# print("JSON Response ", response.json())