# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:06:19 2022

@author: Sümeyra Nihal GELMEZ
"""

a=int(input("please enter your number [0-100]:"))
b=int(input("please  enter your straight number:"))
if a >80:
    a+=10
    print(a)
elif a>60 and a<80:
    a+=5
    print(a)
elif a < 45:
     a-=5
     print(a)
else:
    print(a)
if  b>0 :
   pass
else :
    print(b)
    
     
   
   