# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 14:31:09 2022

@author: Sümeyra Nihal GELMEZ
"""


a=0
num=[]
while a<=10:
    a=a+1
    try:
        number=int(input("enter the number"))
        num.append(number)
    except ValueError:
        print("error")
print(num)

