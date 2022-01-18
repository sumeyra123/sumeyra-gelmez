# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:04:10 2022

@author: Sümeyra Nihal GELMEZ
"""
a=float(input(" please enter is first number?:"))
b=float(input("please enter is second number?:"))
c=input("choose +, -, * or /:")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("incorrect")
