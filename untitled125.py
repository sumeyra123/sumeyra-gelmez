# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:10:17 2022

@author: Sümeyra Nihal GELMEZ
"""



def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

terms = 1000


if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(fibo(i))