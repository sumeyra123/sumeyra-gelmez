# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:01:57 2022

@author: Sümeyra Nihal GELMEZ
"""

#Write a program that reads a temperature value and the letter C for Celsius or F for Fahrenheit. Print whether water is liquid, solid, or gaseous at the given temperature
#at sea level.
# input is string by default
# to use < or > operators 
# you need to convert it to float
num = float(input("Enter a temperature: "))
letter = input("Celsius or Fahrenheit? (Type C or F): ")
# if temperature is less than 0 C
# the water is solid
# if it is between 0 and 100 C
# the water is liquid
# and if it is greater than 100 C
# the water is gaseous
if letter.upper() == "C":
 if num <= 0:
print("Solid")
 elif num < 100:
 print("Liquid.")
 # in this case temperature is greater than 100 C
 else:
 print("Gaseous.")
# the user input is in Fahrenheit
# use the same logic as above 
# 32F = 0C
# 212F = 100C 
else:
 if num <= 32:
 print("Solid.")
 elif num < 212:
 print("Liquid.")
 else:
 print("Gaseous.")