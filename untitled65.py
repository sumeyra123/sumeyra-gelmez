# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:35:22 2022

@author: Sümeyra Nihal GELMEZ
"""

#○P6.2 Write a program that reads numbers and adds them to a list if they aren’t already contained in the list. 
#When the list contains ten numbers, the program displays the
#contents and quits.
#P6.2 Sayıları okuyan ve zaten listede yer almıyorlarsa bunları listeye ekleyen bir program yazın. 
#Liste on sayı içerdiğinde, program içeriği görüntüler ve çıkar. 
values = []
i = 0
while i < 10:
 num = int(input("Enter the number: "))
 # if there is not number num in list yet
 # add it to the list
 # and increment i
 if not num in values:
 values.append(num)
 i = i + 1
 
print(values)
#Counter i ve while döngüsünü kullanın. Her girişten sonra girişin listede olup olmadığını kontrol edin
#ve değilse, listeye ekleyin ve i'yi artırın 