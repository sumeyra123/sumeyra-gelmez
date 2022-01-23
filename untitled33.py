# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:59:40 2022

@author: Sümeyra Nihal GELMEZ
"""

# Write a program that reads four integers and prints “two pairs” if the input consists of two matching pairs (in some order) and “not two pairs” otherwise. For example, 1 2 2 1 two pairs 1 2 2 3 not two pairs
#2 2 2 2 two pairs
# users inputs covert to float 
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
num3 = float(input("Enter a third number: "))
num4 = float(input("Enter a fourth number: "))
# if first and second number are equal
# and third and fourth number are equal
# we have two pairs
if num1 == num2 and num3 == num4:
 print("two pairs")
# if first and third number are equal
# and second and fourth number are equal
# we have two pairs
elif num1 == num3 and num2 == num4:
 print("two pairs")
# and last possibility
# if first and fourth number are equal
# and second and third number are equal
# we have two pair
elif num1 == num4 and num2 == num3:
 print("two pairs")
# in every other case
# we don't have two pairs
else:
 print("not two pairs")