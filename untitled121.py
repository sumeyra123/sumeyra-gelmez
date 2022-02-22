# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:01:13 2022

@author: Sümeyra Nihal GELMEZ
"""

def factoriel(sayı):
    factoriel=1
    while(sayı>=1):
            factoriel*=sayı
            sayı-=1
    print("factoriel",factoriel)



s=int(input("enter the number:"))
factoriel(s)
def avarege(a,b,c):
    return (a+b+c)/3
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
c=int(input("enter the third number :"))
h=avarege(a,b,c)
print("the avarege is :",h)
# tc no
def t