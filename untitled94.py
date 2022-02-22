# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:05:58 2022

@author: Sümeyra Nihal GELMEZ
"""

# 1) Klavyeden girilen bir sayının rakamlarını toplayan programın
 # python kodlarını yazınız.
number=input("please enter your number:")
total=0
for digit in number:
    total+= int(digit)
print("the sum of the digits of the number:",total)
#2) Klavyeden girilen bir cümledeki kelimeleri sayan programın 
#python kodlarını yazınız.
write=input("please enter your anything:")
word=write.split(' ')
print("the text you write:")
print("the words you use: ",word)
print("total words you use:",len(word))
#Klavyeden girilen bir sayının faktöriyelini 
#hesaplayan programın python kodlarını yazınız.
number = int(input("Enter a number to calculate the Factorial:"))
value = 1
for i in range(number):
 value = value * (i+1)
 print("Factorial : ", value)
#Random kullanarak rastgele 0 ile 100 arasında 10 sayı üretiniz. 
import random
a=int(input("please enter your number:"))
dizi=[]
for  i in range (a):
        dizi.append(random.randint(0,100))
print(dizi)