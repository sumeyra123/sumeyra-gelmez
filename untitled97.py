# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:42:55 2022

@author: Sümeyra Nihal GELMEZ
"""
import random
a=int(input("please enter your number:"))
dizi=[]
for  i in range (a):
        dizi.append(random.randint(0,100))
print(dizi)