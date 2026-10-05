#!/usr/bin/env python3

# NOT WORKING

import requests
import xmlrpc.client
import xmlrpc.client as xmlrpclib
from gzip import GzipFile
from io import BytesIO

url = "http://www.pythonchallenge.com/pc/return/disproportional.html"
auth = ('huge', 'file')
res = requests.get(url, auth=auth)

print(res.text)
print('+'*50)



# server = "http://www.pythonchallenge.com/pc/phonebook.php"


# client = xmlrpclib.ServerProxy(server)
# print (client.phone(''))



conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.system.listMethods())


# italy