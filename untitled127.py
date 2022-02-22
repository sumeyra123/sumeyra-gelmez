# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:33:14 2022

@author: Sümeyra Nihal GELMEZ
"""

# def maaş (x):
#     if x>5000:
#         return True
#     else:
#         return False
# for i in maaş :
# filterx=filter(maaş)    


# a=[]
# for i in range(-5,11):
#     a.append(i)
# print(a)
# def poz(b):
#     if b>0:
#         return True
#     else:
#         return False
# pozitive=list(filter(poz,a))
# print(pozitive)
def positifSayı(sayı):
    if sayı >0 :
        return True
    else:
        return False
listem=range(-5,11)
a=filter(positifSayı,listem)
print(list(listem))
print(list(a))    



