# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:10:59 2022

@author: Sümeyra Nihal GELMEZ
"""

# Stereo ses dosyasında okuyan ve sol ve sağ kanalları çeviren bir program yazın. 
# Soldan sağa hareket eden gürültülü bir nesneye sahip bir dosyayla test edin.
import scipy.io.wavfile
import numpy
contents = scipy.io.wavfile.read("music.wav")
samplerate = contents[0]
data = contents[1].tolist()
# swaping left and right channel 
for i in range(len(data)):
 temp = data[i][0]
 data[i][0] = data[i][1]
 data[i][1] = temp 
scipy.io.wavfile.write("output.wav", samplerate, numpy.asarray(data,dtype="int16"))
