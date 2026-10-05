#!/usr/bin/env python3

import requests
import calendar

url = "http://www.pythonchallenge.com/pc/return/uzi.html"
auth = ('huge', 'file')
res = requests.get(url, auth=auth)

print(res.text)
print('+'*50)


for i in range(10, 100):
	year = '1'+str(i)+'6'
	if (calendar.weekday(int(year), 1, 26)) == 0 and int(year)%4 == 0:
		print(year)


# Wolfgang Amadeus Mozart


