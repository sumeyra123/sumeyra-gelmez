# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:01:50 2022

@author: Sümeyra Nihal GELMEZ
"""

#Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin 
# alanını hesaplayan Python programı yazınız.
# def rectangler_area(width,height):
#     area=float(width)*float(height)
#     return area
# a=input("width:")
# b=input("height:")
# area=rectangler_area(a, b)
# print(area)
# #Girilen sayının faktöriyelini fonksiyon kullanarak hesaplayan
# # Python programını yazınız. 
def factoriel(sayı):
    factoriel=1
    if(sayı==0 or sayı ==1):
        print("factoriel",factoriel)
    else:
        while(sayı>=1):
            factoriel*=sayı
            sayı-=1
        print("factoriel",factoriel)
# # Kullanıcının girdiği 3 sayının ortalamasını fonksiyon 
# # kullanarak hesaplayan Python programını yazınız.   
# def average(x,y,z):
#   return  (x, y, z)/3
# a=average(1,2,3)
# print(a)
# # tek çift sayı hesaplama
# def find(num):
#     # code logic here
#     numtype = "odd"
#     if num%2 == 0:
#         numtype="even"
#     return numtype

# num = int(input('Enter the number: '))      # take your input
# numtype = find(num)                         # call the find function
# print('Given number is',numtype)            # print if the number is even or odd 
# # D= A+B*C2 
# # 6- A, B ve C değerlerini kullanıcıdan alarak D değerini 
# # hesaplattırıp sonucu ekrana yazdıran Python programını yazınız.

