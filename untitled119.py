# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:08:03 2022

@author: Sümeyra Nihal GELMEZ
"""

def find(num):
    # code logic here
    numtype = "odd"
    if num%2 == 0:
        numtype="even"
    return numtype

num = int(input('Enter the number: '))      # take your input
numtype = find(num)                         # call the find function
print('Given number is',numtype)            # print if the number is even or odd6
