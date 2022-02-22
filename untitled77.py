# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:05:19 2022

@author: Sümeyra Nihal GELMEZ
"""

# Write a function that reverses the sequence of elements in a list. For example, 
# if you call the function with the list 1 4 9 16 9 7 4 9 11
# then the list is changed to
# 11 9 4 7 9 16 9 4 1
# input list must have even length
def swapHalves(values):
 # iterator for the left half
 posL = 0
 # iterator for the right half
 posR = len(values) // 2
 # iterate over element in the left half
 while posL < len(values) // 2:
 # and swap it with appropriate value in the right half
 temp = values[posL]
 values[posL] = values[posR]
 values[posR] = temp
 # increment positions
 posL = posL + 1
 posR = posR + 1
 
values = [9, 13, 21, 4, 11, 7, 1, 3]
swapHalves(values)
values # prints [11, 7, 1, 3, 9, 13, 21, 4]
