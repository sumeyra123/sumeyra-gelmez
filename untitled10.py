# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:26:24 2022

@author: Sümeyra Nihal GELMEZ
"""
a=int(input("please enter your weather condition:"))
if a>= 0 and  a<= 5:
  print("cold")
elif a >= 6 and a<=14 :   
  print("warm")
elif a>=15:
  print("hot") 
else:
 print("enter the appropriate temperature")   