# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:26:22 2022

@author: Sümeyra Nihal GELMEZ
"""
while True:
     num1=input("First number(Press e to EXIT):")
     if num1=="e" or "E":
         break
     num2=input("second number:")

     try:
         number1=int(num1)
         number2=int(num2)
         print(number1,"/",number2,"=",number1/number2)
     except (ValueError,ZeroDivisionError):
         print("Error. Try again!")