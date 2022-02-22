# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:36:54 2022

@author: Sümeyra Nihal GELMEZ
"""
total=1
a=int(input("please enter your number : "))
for  i in range (a):
    if a%2==0:
     total=total+i
    print("double numbers total",total)