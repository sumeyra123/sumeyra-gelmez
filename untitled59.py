# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:52:31 2022

@author: Sümeyra Nihal GELMEZ
"""
value=0
a=int(input("please enter your number:"))
for  i in range (2,a):
     if a%i==0:
         value+=1
         break
if value!=0:
         print("not prime number")
else:
         print("prıme number")
         
   