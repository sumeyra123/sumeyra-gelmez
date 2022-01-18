# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:32:43 2022

@author: Sümeyra Nihal GELMEZ
"""

visa1 = int(input("Visa1:"))
visa2 = int(input("Visa2:"))
final = int(input("Final:"))
general_note=  (visa1 * 3/10 + visa2 * 3/10 + final * 4/10)
if (general_note >= 60):
     print("left")
elif (final <=50): 
     print("left")    
else:
    print("passed")
    
         
         
          