# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:07:44 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bir ses dosyasını okuyan, tüm değerleri tersine çeviren ve sonucu kaydeden bir program yazın.
#  Konuşma kaydı veya bir şarkı ile deneyin.
import scipy.io.wavfile
import numpy
contents = scipy.io.wavfile.read("music.wav")
samplerate = contents[0]
data = contents[1].tolist()
# iterate from the last element to the first 
# and add it to new output data
outputdata = []
for i in range(len(data) - 1, -1, - 1):
 outputdata.append(data[i])
scipy.io.wavfile.write("output.wav", samplerate, numpy.asarray(outputdata,dtype="int16"))