# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:39:37 2022

@author: Sümeyra Nihal GELMEZ
"""

#2'den 10.000'e kadar olan tüm sayıları bir listeye ekleyen bir program yazın. 
#Ardından 2'nin katlarını (ancak 2 değil), 3'ün katlarını (ancak 3'ü değil) vb. 100'ün katlarına kadar kaldırın.
# Kalan değerleri yazdırın. 
# removes all multiples of num (but not num) in list values
def removeMultiples(values, num):
 i = 0
 # iterate over all elements
 while i < len(values):
 # current element is equal to num
 # so increment i (go to next element)
if values[i] == num:
  i = i + 1
 # remainder after division by num is zero
 # it means that current element is multiple of num
 elif values[i] % num == 0:
 # so remove it from the list
 # notice: we do not need to increment i
 # because next element is now at position i 
 values.pop(i)
 # current element is not num and it is not multiple of num
 # go to the next element
     else:
 i = i + 1
values = []
# adds all numbers from 2 to 10000 (included) to a list
for i in range(2, 10001):
 values.append(i)
# removes multiples of 2, 3, ..., 100
for num in range(2, 101):
 removeMultiples(values, num)