# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:10:53 2022

@author: Sümeyra Nihal GELMEZ
"""
#Write a program that translates a number between 0 and 4 into the closest letter grade. For example, the number 2.8 (which might have been the average of several grades) would be converted to B–. Break ties in favor of the better grade; for exam ple
#2.85 should be a B
num = float(input("Enter a number: "))
if 0 <= num < 0.35:
 print("F")
elif 0.35 <= num < 0.85:
 print("D-")
elif 0.85 <= num < 1.15:
 print("D")
elif 1.15 <= num < 1.5:
 print("D+")
elif 1.5 <= num < 1.85:
 print("C-")
elif 1.85 <= num < 2.15:
 print("C")
elif 2.15 <= num < 2.5:
 print("C+")
elif 2.5 <= num < 2.85:
 print("B-")
elif 2.85 <= num < 3.15:
 print("B")
elif 3.15 <= num < 3.5:
 print("B+")
elif 3.5 <= num < 3.85:
 print("A-")
else:
 print("A")
