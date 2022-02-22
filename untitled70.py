# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 10:21:17 2022

@author: Sümeyra Nihal GELMEZ





meyveler=["elma","çilek","armut"]
alişveril_listesi=["süt","peynir","meyveler"]
meyveler.extend(alişveril_listesi)
print(meyveler)

bellekler=["ram ","rom"]

ekran_kartları=["paylaşımlı","paylaşimsiz"]
sabit_diskler=["sssd"]
birimler=bellekler,ekran_kartları,sabit_diskler
print(birimler)
"""
sozluk={"bilim insanı":"aziz sancar","şair":"m.akif","astronomi":"ali kuşçu"}
notlar={"erdal":98,"arzu":99,"sümeyra":50}
a=input("please enter your name:")
b=int(input("please enter your mark:"))
notlar[a]=b
print(notlar)
ogrenciNotlari={"Arzu":90,"Erdal":60,"Sumeyra":70,"Dua":90,"Meryem":100,"Yaren":90}
top=0
for i,j in ogrenciNotlari.items():
    print("Öğrenci Adı: {0}\t Notu :{1}".format(i,j))
    top+=j
print("Ortalama :{}".format(top/len(ogrenciNotlari)))
print(del(0)
      if "sagilik merkezi" in onemli_telefonlar:
    print("var")
else:
    print("yok")
kume={"python","c","4","cahit"}
print(len(kume))