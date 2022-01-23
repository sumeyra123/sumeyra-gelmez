# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:39:33 2022

@author: Sümeyra Nihal GELMEZ



for i in range (1,20):
   if i%3==0:
      break
   print(i)
print("merhaba")
"""
i=1
while i>=10:
    print (i)
    i=i-1
print("merhaba")    
#pozitif sayılarını toplamı-negatif sayıların sayısı
total=0
negative_numbers=0
numbers=[10,23,-5,0,-8,-1,3,-9]
for number in numbers:
    if number >0 :
     total=total+number
    elif number <0:
        negative_numbers=negative_numbers +1
print("negative number  =", negative_numbers)
print("positive numpers total=:",total)
#
number = int(input("Enter a number to calculate the Factorial:"))
value = 1
for i in range(number):
 value = value * (i+1)
 print("Factorial : ", value)
 
#
fakt=1
i=2
while fakt<0:
    fakt*=i
    i += 1
print("Faktöriyel=", fakt)
#
a=int(input("please enter your number:"))
b=int(input("please enter your 2. number :"))
for i in range (5,10):
    print (i)      
