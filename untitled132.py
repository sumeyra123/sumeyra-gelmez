# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:29:06 2022

@author: Sümeyra Nihal GELMEZ
"""

# ****** İŞLEM SEÇİM EKRANI ******
# Çıkış (0)
# Öğrenci Ekleme (1) 
# Ada Göre Öğrenci Sorgulama (2)
# Öğrenci Sil (3)
# Kayıt Güncelle (4)
# Tüm Öğrencileri Listele (5)
# Lütfen işlem seçiniz :
import sqlite3 as lite
vt=lite.connect("C:\SQLite\database.db")
im=vt.cursor()   

def ogrenciListele():
  sorgu="SELECT* FROM Ogrenci"
  im.execute(sorgu)
  veri=im.fetchall()
  vt.commit()
  for i in veri:
      print(i)
def ogrenciEkle(ad,soyad):
    sorgu="INSERT INTO Ogrenci(ad,soyad) VALUES(?,?)"
    im.execute(sorgu ,(ad,soyad))
    vt.commit()
def ogrenciara(ad):
    sorgu="SELECT *FROM Ogrenci WHERE Ad LIKE '"+ad+"%'"    
    im.execute(sorgu)
    veri=im.fetchall()
    vt.commit()
    return veri
def ogrenciSil(id):
     sqlcumle="DELETE FROM Ogrenci WHERE Ogrenci_No='"+id+"'"
     im.execute(sqlcumle)
     vt.commit()
     ogrenciListele()
text="""
# ****** İŞLEM SEÇİM EKRANI ******
# Çıkış (0)
# Öğrenci Ekleme (1) 
# Ada Göre Öğrenci Sorgulama (2)
# Öğrenci Sil (3)
# Kayıt Güncelle (4)
# Tüm Öğrencileri Listele (5)
# Lütfen işlem seçiniz :
"""
sonislem="İSLEM YOK"
def topluSil(basID,bitID):
    for i in range  (basID,bitID+1):
        ogrenciSil(str(i))
    ogrenciListele()
while True:
  secim=int(input(text))
  if secim==0:
      onay=input("çıkış yap.emin misiniz(E/H)")
      if onay.upper()=='E':
          break
      else:
          pass
  elif secim==1:
      ad=input("ogrenci adı:")
      soyad=input("ogrenci soyadı")
      ogrenciEkle(ad, soyad)
      ogrenciListele()
  elif secim==2:
       pass
  elif secim==3:
      adara=input("ogrenci adı :")
      ogrenciara(adara) 
  elif secim==4:
        pass
  elif secim==5:
        silID=input("silincek ogrenci ıd giriniz:")
        ogrenciSil(silID)
  elif secim==6:
    print(ogrenciListele()) 
  elif secim==7:
       başlama=int(input("ilk ıd :"))
       bitis=int(input("bitis ıd:"))
       topluSil(başlama,bitis)
  elif secim==9:
      print(sonislem)
  else:
      print("hatalı işlem")  
        
         
      
    
    
     
     
    