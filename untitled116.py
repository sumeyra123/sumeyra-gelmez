# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:27:42 2022

@author: Sümeyra Nihal GELMEZ
"""

# return fonksinıyonu işlem bittikten sonra çağrildiği yere değer döndürmesidir
# def toplama (a,b,c):
#     print("toplama ",a,b,c)
# def ikiyleçarp (a):
#    print("ikiyle çarp",a*2)
# toplam=toplama(3,4,5)
# ikiyleçarp(toplam)
# def toplama(a,b,c):
#  return a+b+c
# def ikiyleçarp(a):
#  return a*2
# toplam=toplama(3,4,5)
# print(ikiyleçarp(toplam)) 
# fonksiyonlarda çağridıği yere herhangi bir değer döndürmeyen(return )kullanılmayan fonksiyonlara void denir. 
# def selamla (isim) :
#     print("selam",isim)
# selamla("murat")    
# # selamla("serhat")
# def selamla(isim="isimsiz"):
#     print("selam",isim)
# selamla()   #isismsiz bir değer atadım ve onu karşıladı
# def bilgilerigöster(ad,soyad,no):
#     print("ad:",ad,"soyad:",soyad,"no:",no)
# bilgilerigöster("murat", "hallek", 12345)    
# def toplama(*a):
#     print(a)
# toplama(1,2,3)#bir tuple içinde tutulmuştur.
def toplama (*a):
 toplam=0#toplam değişkeni oluşturalım
 for i in a:
  toplam+=i
  print(toplam)
  
toplama(1,2,3,4,5)    