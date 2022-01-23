# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:51:21 2022

@author: Sümeyra Nihal GELMEZ
"""

#Desibel (dB) birimlerindeki L ses seviyesi L = 20 log10 (p / p0) ile belirlenir.
#burada p, sesin ses basıncıdır (Paskallarda, kısaltılmış Pa) ve p0, 20 × 10-6 Pa'ya eşit bir referans sestir (burada L 0 db'dir). Aşağıdaki tabloda belirli ses seviyelerinin açıklamaları verilmiştir. Ağrı eşiği
#1 m'de olası işitme hasarı Kriko çekiç
#Sakin kütüphane © Photobuff/iStockphoto. Hafif yaprak hışırtısı
#130 dB 120 dB 100 dB
#Yoğun bir karayolunda trafik 10 m 90 dB Normal konuşma
#60 dB 30 dB 0 dB
#Bir değer ve birim, dB veya Pa okur ve sonra yazdırır bir program yazın
#yukarıdaki listeden en yakın açıklama.
import math 
value = float(input("Enter a value: "))
unit = input("Enter an unit (dB or Pa): ")
# if user enters a sound pressure of the sound (Pa)
# convert it to dB using given formula
# because given table is in decibels 
if unit.lower() == "pa":
 # log(num, base) returns the logarithm base "base" of "num" 
 L = 20*math.log(value / (20 * 10**(-6)), 10)
# input is sound level (dB)
else:
 L = value
 
# find out in which interval L belongs
# and print corresponding message
if L <= 15:
print("Light leaf rustling")
elif 15 < L <= 45:
 print("Calm library")
elif 45 < L <= 75:
 print("Normal conversation")
elif 75 < L <= 95:
 print("Traffic on a busy roadway at 10 m")
elif 95 < L <= 110:
 print("Jack hammer at 1 m")
elif 110 < L <= 125:
 print("Possible hearing damage")
else: 
 print("Threshold of pain")
