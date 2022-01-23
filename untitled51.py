# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:09:08 2022

@author: Sümeyra Nihal GELMEZ
"""

a=int(input("please enter your number:"))
b=int(input("please neter your 2. number:"))
if a <b :
  for i in range (a,b+1):
      print (i)
else:
     for i in range (a,b-1,-1):
      print (i)
          