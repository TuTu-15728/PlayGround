#!/usr/bin/env python3

import requests


url = "http://www.pythonchallenge.com/pc/hex/idiot2.html"
url_2 = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
auth = ("butter", "fly")

res = requests.get(url, auth=auth)
headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}



# for head in range(30202, 2123456789):
# 	headers['Range'] = 'bytes='+ str(head) + '-2123456789'
# 	res_2 = requests.get(url_2, auth=auth, headers=headers)
# 	print(res_2.text)

my_zip = open('invader.zip', 'wb')

headers['Range'] = 'bytes='+ str(1152983631) + '-2123456789'
res_2 = requests.get(url_2, auth=auth, headers=headers)
# print(res_2.text)

my_zip.write(res_2.content)

# invader
# esrever ni emankcin wen ruoy si drowssap eht
# and it is hiding at 1152983631.

# zip password "redavni"