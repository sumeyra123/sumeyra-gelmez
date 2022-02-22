# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:09:36 2022

@author: Sümeyra Nihal GELMEZ
"""

# def yazdır(**kwargs):#key,values
#     print(kwargs)
# yazdır(ahmet=20,ayşe=65,ebru=98)    
def yazdir(*args,**kwargs):
    print(kwargs)
    print(args)
yazdir('fatma','veli','sümeyra',sümeyra=22,ahmet=17,ebru=18,ayşe=19,duuaa=25)   

#önce args sonra kwargs kullanılır ıkısınıde kullancakdak



def nothesapla(**kwargs):
    print(kwargs)
    vizenotu=0
    finalnotu=0
    for i, j in kwargs.items():
       if i=="vize":
        vizenotu=j
       elif i=="final":
         finalnotu=j
       return vizenotu*0.4,+0.6*finalnotu
sonuc=nothesapla(ad="erdal",vize=50,final=100)
print(sonuc)   
   #items adlardır
for i,j in kwargs.items():
       print(i,j)
sonuc=nothesapla(ad="erdal",vize=50,final=100)       