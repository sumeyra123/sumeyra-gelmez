# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:47:02 2022

@author: Sümeyra Nihal GELMEZ
"""

# def selammla(*isim):
#        print("selam",*isim)
# selammla("arzu","erdal","can")    


# def selam(*args):
#     for i in args:
#         print("selam",args)
# print(selam('duaa'))




# def average(*args):
#     av=0
#     for i in args:
#         av=av+i/len(args)
#         print(av)
# average(3,4)

# def nothesapla(v1,v2,final,ogrenci="erdal"):
#     ortalama=((v1+v2)*0.4)+(final*0.6)
#     return ortalama ,ogrenci
# sonuc=nothesapla(v1=100,final=60)
# print(sonuc)
# #bir liste üretsin.listenın uzunluğu belirlesin.1 ile 100 arasında belirltilensayılar
def listeuret(n):
  liste=[]
   while len(liste)<n:
     deger=rnd.randint(1,100)
    if deger liste in liste:
        pass
    else:
        liste.append(deger)
   return liste
mylist=listeuret(18)
print(mylist)


mylist2=filter(lambda n:n%2!=0,mylist)
