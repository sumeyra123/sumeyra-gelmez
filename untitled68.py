# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 10:43:36 2022

@author: Sümeyra Nihal GELMEZ

liste=[1,3,5,7,9,11,13,15,17,19]
print(liste[0:6])
print(liste[2:5])
print(liste[3:8])
print(liste[:5])
print(liste[3:])
print(liste[0:8:2])
print(liste[::3])

takımlar=["gs","fb","bjk"]
takımlar.append("ts")
print(takımlar)

sebzeler =["lahana","marul","ıspanak","fasulye"]
sebzeler.insert(2,"patlıcan")
print(sebzeler)
"""
iller1=["istanbul","ankara","samsun","amasya"]
iller2=iller1.copy()
print(iller2)

takımlar=["gs","fb","bjk","ts","hatayspor","fb","bjk","gs"]
say1=takımlar.count("gs")
say2=takımlar.count("fb")
print(say1,say2)


sehir1=["adana","istanbul","almanya","izmir","ankara"]
sehir2=["burdur","van","muş"]
sehir1.extend(sehir2)
print(sehir2)
sehir2.sort()
print(sehir1)

sebzeler=["lahana","marul","pırasa","ıspanak","fasulye"]
print(sebzeler.index("ıspanak"))
iller=["adana","istanbul","almanya","izmir","ankara"]
print(iller.index("adana"))