# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:58:15 2022

@author: Sümeyra Nihal GELMEZ
"""

even=[]
odd=[]
a=0
while a<10:
    sayi=int(input("sayi gir:"))
    if sayi%2==0:
        even.append(sayi)
    else:
         odd.append(sayi)
  
   
print(even)
print(odd)
