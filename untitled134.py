# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:25:21 2022

@author: Sümeyra Nihal GELMEZ
"""
def main():
  a=int(input("please enter your mark :"))
  print(puan(a))
def puan (digit):
    if digit <=0 or digit  <=50:return"one"
    if digit <=50 or digit <=60:return "two"
    if digit <=60 or digit <=70 :return"three"
    if digit <=70 or digit <=85:return "four"
    if digit <=85 or digit <= 100:return "five"
main()
       #100 den fazla girildiğide none hatası vermektedir.