# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:46:33 2022

@author: Sümeyra Nihal GELMEZ
"""

# kullanıcıdan 10 sayı iste 
# tek sayı ise ayrı bir liste çift sayı i,se ayrı bir listeye yazdir.
odd=[]
even=[]
a=int(input("please enter your number:"))
for  i in range(10):
    
 if a % 2 ==0:
   even.append(a)
else:
  odd.append(a)
  a+=1
  print(odd)
  print(even)
    
    
