# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:06:29 2022

@author: Sümeyra Nihal GELMEZ
"""

def ciftMi(x): 
    return x % 2 == 0
 
toplam=0
sayac=0
baslangic = input("Başlangıç Sayısı :")
bitis = input("Bitiş Sayısı :")
for sayi in range (int(baslangic), int(bitis)+1):
    if(ciftMi(int(sayi))):
        toplam=toplam+sayi
        sayac=sayac+1
print('Ortalama',(toplam/sayac))