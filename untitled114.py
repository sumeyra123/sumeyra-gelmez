# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:48:14 2022

@author: Sümeyra Nihal GELMEZ
"""

# def alan_hesapla(r):
#    alan=3.14*r**2
#    return alan
# x= alan_hesapla(5)
# print(x)

# def çevre_hesapla(r):
#     çevre=2*3.14*r
#     return çevre
# x=çevre_hesapla(2)
# print(x)

# def alan(r):
#     return 3.14*r**2
# def cev(r):
#     return 2*3.14*r
# a=int(input("capi:"))
# print("alan=",alan(a))
# print("cevre=",cev(a))

import sqlite3#sqlkullamak için sqlite3 kütüpkanesını kodlarını ekliyoruz

vt=sqlite3.connect("c:\sqlite\database.db")#veritabanı bağlantısını sağlar
im=vt.cursor()#imleç(cursor) olustumatya yaşar.cursor veritabanındaki sql sorgularını çaliştırmanı sağlar.



sorgu="SELECT * FROM ogrenci"
im.execute(sorgu)#imlecin sql cümlesini yürütmesini sağlar(execute)

veri=im.fetchall()#select sonucunda gelen tüm değerleri olmayı sağlar.veri isimli değişkene atadık.

vt.commit()#yukarıdakı işlemleri uygula,çaliştir demektir.
print(veri)#select sonucunda gelen değerler veri isimli değişlkende ,onu yazdırıyoruz.

# sorgu="SELECT *FROM ogrenci WHERE ogrenci_no='101'"
# im.execute(sorgu)
# veri=im.fetchall()
# vt.commit()
# print(veri)

sorgu2="Select Ders_adı FROM Dersler Where Sınıf='1' OR Sınıf='2'"

