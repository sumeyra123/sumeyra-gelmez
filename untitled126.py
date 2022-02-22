# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 10:17:58 2022

@author: Sümeyra Nihal GELMEZ
"""

# liste=range(20)
# filter1=filter(lambda sayı:sayı %2!=0,liste)
# print(list(filter1))#filter fonk true false döndürür,true oluna listeye çevirir.

# no=[23,56,87,47,1,2,36,45,47]
# isim=["ahmet","mehmet","ayşe","elif","kemal","zeynep","fatma","can"]
# zip1=zip(no,isim)
# print(list(zip1))

# liste1=[1,6,8,9,25,36,14,52,69,21]
# liste2=[3,5,25,14,41,36,58,60,20,30]
# for i,j in zip(liste1,liste2):
#     filter1=filter(lambda i:i%3==0,liste1)
#     filter2=filter(lambda j:j %5==0,liste2)
# print("3 kat",list(filter1))
# print("5 kat",list(filter2))

# def üçünkatı(n):
#     if n%3==0:
#         return true
#     else:
#         return false
    
    
# isim=["ahmet","mehmet","veli","ali"]
# maas=[1000,2000,3000,4000]
# zip1=zip(isim,maas)
# print(list(zip1))    #zipin yaptiği 1, elemnla 2. elemanla birleştir.sırayla
    
liste=["ahmet","mehmet","veli","ali"]
maaş=[5000,6000,7000,1000,2000,3000,4000]
filter1=filter(lambda a:a>5000,maaş)
maaş1=list(filter1)   
print(list(maaş1))
print(list(liste)) 