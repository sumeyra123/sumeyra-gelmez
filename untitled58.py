# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:30:00 2022

@author: Sümeyra Nihal GELMEZ
"""

#PROGRAMMİNG EXERCİCES
#P6.1 Write a program that initializes a list with ten random integers and then prints four lines of output, 
#containing • Every element at an even index. • Every even element. • All elements in reverse order.
#• Only the first and last element.
# because we want use randint() method
import random
values = []
for i in range(10):
 # we add random integer between -100 and 100
 values.append(randint(-100, 100))
 
print("Elements at even indexes: ")
# i iterates over the set {0, 2, 4, 6, 8}
# 0 is start parameter, 10 is stop parameter (excluded)
# and 2 is step parameter in range(start, stop, step) method
for i in range(0, 10, 2):
 print(values[i])
print("Even elements: ")
for i in range(10):
 # if remainder after division by 2 is 0
 # number is even
 if values[i] % 2 == 0:
 print(values[i])
 
print("Reverse order: ")
# i iterates ove the set {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
for i in range(9, -1, -1):
 print(values[i])
 
print("First element is " + str(values[0]) + " and last element is " +str(values[9]))