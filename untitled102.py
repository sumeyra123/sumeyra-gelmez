# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:14:27 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bir ses dosyasını okuyan ve bir yankı tanıtan bir program yazın. 
# Her veri değeri için 0,2 saniye önceki değerin yüzde
#  80'ini ekleyin. İşiniz bittiğinde, hiçbir değer 32.787'den büyük olmayacak 
#  şekilde sonucu yeniden ölçeklendirin.
import scipy.io.wavfile
import numpy
contents = scipy.io.wavfile.read("10sec.wav")
samplerate = contents[0]
data = contents[1].tolist()
outputdata = []
for i in range(len(data)):
 # in first 0.2 sec we don't have echo 
  if i <= samplerate * 0.2:
   outputdata.append(data[i])
 # data[int(i - 0.2 * samplerate)]
 # is the sound that passed 0.2 second ago
 # multiply it by 0.8, because we want 80% of the value
 # and add to the current sound (data[i])
else:
 outputdata.append(data[i] + 0.8 * data[int(i - 0.2 * samplerate)]

# rescalling values so that 
# all values are in range (-32787, 32787) = (a, b)
# use formula: newValue = (b - a)*(x - min)/(max - min) + a
maximumValue = max(outputdata)
minimumValue = min(outputdata)

outputdata2 = []
for i in range(len(outputdata)):
 value = (32787 + 32787) * (x - minimumValue) / (maximumValue - minumumValue )-32787
 outputdata2.append(value) 
scipy.io.wavfile.write("output.wav", samplerate, numpy.asarray(outputdata2,dtype="int16"))