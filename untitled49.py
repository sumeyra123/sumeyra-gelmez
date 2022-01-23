# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:47:54 2022

@author: Sümeyra Nihal GELMEZ

cities=["kocaeli,rize","antalya","koyseri","hatay"]
for city in cities :
    if  len(city)<=5 :
     print(city)

total=0
cities=["kocaeli","rize","antalya","koyseri","hatay"]
for i in (cities):
    if len(i)<=5:
        total =total+1
        print(i)
print ("cities:",total)
"""
numbers=[0-10]
toplam=0
i=1
while i<= 10 :
     if(i%2!=0):
         print(i)
     i=i+1
#wkile dögüsü kendi kendini döndüremez onun için artiş yapmak zorundayım.
for i in range(0,6,3):
 print(i)     