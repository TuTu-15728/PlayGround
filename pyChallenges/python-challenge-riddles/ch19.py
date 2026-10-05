#!/usr/bin/env python3

import requests
import re
import base64
import soundfile
from soundfile import SoundFile



# url = "http://www.pythonchallenge.com/pc/hex/bin.html"
# auth = ("butter", "fly")

# response = requests.get(url, auth=auth)
# print(response.text)
# my_data = re.findall(r'base64\n\n(.*?)\n\n--==', response.text, re.DOTALL)
# print(my_data[0])
# print("+"*50)


# my_wav = open('indian.wav', 'wb')
# my_wav.write(base64.b64decode(my_data[0]))



my_sf = soundfile.SoundFile('indian.wav')

print(my_sf.read)

soundfile.write('ew_indian.wav', my_sf.read(), my_sf.samplerate, my_sf.subtype, 'BIG', 'WAV')

new_sf = soundfile.SoundFile('new_indian.wav')


# Play using mplayer




