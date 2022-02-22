# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:01:13 2022

@author: Sümeyra Nihal GELMEZ
"""

# Stereo ses dosyasında okuyan ve her örnek için (sol - sağ) / 2 içeren bir mono dosya 
# üreten bir program yazın. Şarkıların ses dosyalarıyla test edin. Dosya, şarkıcının 
# sesini her iki kanalda da eşit olarak kaydederse, sonuç enstrümanı içerecektir.
# zihinsel müzik ve vokalleri çıkarın!
import scipy.io.wavfile
import numpy
contents = scipy.io.wavfile.read("music.wav")
samplerate = contents[0]
data = contents[1].tolist()

outputdata = []
 
for i in range(len(data)):
  x = (data[i][0] - data[i][1]) / 2
  outputdata.append(x)
scipy.io.wavfile.write("output.wav", samplerate, numpy.asarray(outputdata,dtype="int16"))