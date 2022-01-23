# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:03:58 2022

@author: Sümeyra Nihal GELMEZ
"""

#The boiling point of water drops by about one degree Celsius for every 300 meters (or 1,000 feet) of altitude. Improve the program of Exercise P3.9 to allow the user to
#supply the altitude in meters or feet.
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
 
# if altitude is in meters 
# the boiling point of water drops by one degree
# for every 300 meters
# altitude / 300 is that number of degrees 
if letterAlt.upper() == "M":
 diff = altitude / 300
# or altitude / 1000 if altitude is in ft
else:
 diff = altitude / 1000
 
# 0 - diff is the freezing point of water
# 100 - diff is the boiling point of water
# at given altitude
if num <= 0 - diff:
 print("Solid.")
elif num < 100 - diff:
 print("Liquid.")
else:
 print("Gaseous.")
