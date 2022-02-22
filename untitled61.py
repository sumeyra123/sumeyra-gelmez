# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:05:49 2022

@author: Sümeyra Nihal GELMEZ
"""

 
number = int(input('Enter the Number : '))

oddtotal=0
doubletotal=0
for i in range(1,number):
  if(i%2==0):
    doubletotal+=i
else:
    oddtotal+=i
print("Sum of Odd Numbers:"+ str (oddtotal))
print("Sum of Even Numbers:"+str(doubletotal)) 