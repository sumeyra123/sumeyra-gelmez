# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:06:17 2022

@author: Sümeyra Nihal GELMEZ
"""

#Add error handling to Exercise P3.10. If the user provides an invalid unit for the altitude, print an error message and end the program
# input is string by default
# to use < or > operators 
# you need to convert it to float
num = float(input("Enter a temperature: "))
letterTemp = input("Celsius or Fahrenheit? (Type C or F): ")
altitude = float(input("Enter an altitude: "))
letterAlt = input("Meters or feet? (Type m or ft): ")
# formula for converting Fahrenheit to Celsius is
# C = (F - 32) / 1.8 
if letterTemp.upper() == "F":
 num = (num - 32) / 1.8
# if temperature unit of measurement is nor C nor F
# print "Inavlid input"
# and end the program
elif letterTemp.upper() != "C":
 raise Exception("Invalid input.")
 
# if altitude is in meters

# if altitude is in meters 
# the boiling point of water drops by one degree
# for every 300 meters
# altitude / 300 is that number of degrees 
if letterAlt.upper() == "M":
 diff = altitude / 300
# or altitude / 1000 if altitude is in feets
elif letterAlt.upper() == "FT":
 diff = altitude / 1000
# if the altitude unit of measurement
# is not m nor ft
# print "Inavlid input"
# and end the program 
else:
 raise Exception("Invalid input.")
 
# 0 - diff is the freezing point of water
# 100 - diff is the boiling point of water
# at given altitude
if num <= 0 - diff:
 print("Solid.")
elif num < 100 - diff:
 print("Liquid.")
else:
 print("Gaseous.")