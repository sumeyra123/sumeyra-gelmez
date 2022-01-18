# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:48:45 2022

@author: Sümeyra Nihal GELMEZ
"""

height= float(input("please enter your height:"))
weight = int(input("please enter your weight:"))
bki =  weight / (height ** 2)
if(bki >= 18.5 and bki <= 25):
    print("medium")
elif (bki >= 25 and bki <= 55):
    print("more fat")
elif (bki >= 56 and bki <= 70):    

    print("obese")
else:
    print("not defined")