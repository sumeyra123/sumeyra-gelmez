# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:33:58 2022

@author: Sümeyra Nihal GELMEZ
"""

a="arzu ,erdal ,ali ,cansu"
notlar=[60,70,80, 90, 100]
student =a.split(",")
karne =dict()
for  i in range (5):
   karne[student [i]]=notlar=[i]
   print(karne)
