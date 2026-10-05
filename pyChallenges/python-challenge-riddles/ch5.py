#!/usr/bin/env python3

import requests
import pickle



url = "http://www.pythonchallenge.com/pc/def/peak.html"
res = requests.get(url)


with open('banner.p', 'rb') as f:
    data_loaded = pickle.load(f)

for i in range(len(data_loaded)):
	print()
	for j in range(len(data_loaded[i])):
		print((data_loaded[i][j][0] * data_loaded[i][j][1]), end="")


newurl = "http://www.pythonchallenge.com/pc/def/channel.html"


