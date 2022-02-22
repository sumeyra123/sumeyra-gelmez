# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:02:50 2022

@author: Sümeyra Nihal GELMEZ
"""

# Compute the alternating sum of all elements in a list. For example, if your program reads the input
# 1 4 9 16 9 7 4 9 11 then it computes
# 1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = –2
def alternatingSum(values):
 sum = 0
 pos = 0
 while pos < len(values):
 # if element is at even position
 # add it to the sum
 if pos % 2 == 0:
 sum = sum + values[pos]
 # else, if element is at odd position
 # subtract it from the sum
 else:
 sum = sum - values[pos]
 pos = pos + 1
 return sum
 
values = [1, 4, 9, 16, 9, 7, 4, 9, 11]
alternatingSum(values) # prints -2
#