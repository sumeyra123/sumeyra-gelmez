# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 16:24:44 2022

@author: Sümeyra Nihal GELMEZ
"""

# liste=[1,2,3,4,5,6,7,8]
# def kareal(sayı):
#     return sayı**2
# map1=map(kareal,liste)
# map1=list(map1)
# print(map1)

# liste=[1,2,3,4,5,6,7,8]
# map2=map(lambda sayı:sayı**2,liste)
# print(list(map2))


# liste1=[1,3,5,7,9,11]
# liste2=[6,7,8,9,4,6]
# liste3=[8,4,9,3,1,5]
# map2=map(lambda x,y,z:x*y*z ,liste1,liste2,liste3)
# print(list(map2))
from functools import reduce
liste=[0,1,2,3,4,5,6]
reduc1=reduce(lambda x,y: x+y,liste)
print(reduc1)

def  karşilaştırma(x,y):
    if x>y:
        