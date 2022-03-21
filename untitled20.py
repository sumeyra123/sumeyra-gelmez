# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:01:58 2022

@author: Sümeyra Nihal GELMEZ
"""

# "r"‎ - Oku - Varsayılan değer. Dosya okuma için bir dosya açar, dosya yoksa hata‎

# "a"‎ - Ekle - Bir dosyayı ekleme için açar, yoksa dosyayı oluşturur‎

# "w"‎ - Yazma - Bir dosyayı yazmak için açar, yoksa dosyayı oluşturur‎

# "x"‎ - Oluştur - Belirtilen dosyayı oluşturur, dosya varsa bir hata döndürür‎


# demofile.txt

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!


f=open("demofile.txt","r")
print(f.read())#dosyayı actim



#path ie açma
f=open("D:\\myfiles\welcome.txt","r")
print(f.read())

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f=open("demofile.txt","r")
print(f.read(5))

#♣readline()fonksiyonu sadce satır satır okur
f=open("demofile.txt","r")
print(f.readline())
print(f.radline())

# ‎Dosyanın satırlarını döngüye alarak, tüm dosyayı satır satır okuyabilirsiniz:‎


f=open("demofile.txt","r")
for x in f :
    print(x)


#close files‎Not:‎‎ Dosyalarınızı her zaman kapatmalısınız, bazı durumlarda arabelleğe alma nedeniyle, dosyayı kapatana kadar bir dosyada yapılan değişiklikler gösterilmeyebilir.‎
f=open("demofile.txt","r")
print(f.readline())
f.close()


# "a"‎ - Ekle - dosyanın sonuna eklenir‎

# "w"‎ - Yazma - mevcut içeriğin üzerine yazar‎


f=open("demofile.txt","a")
f.write("now the file has more content")
f.close()
#dosyayı okuyalım
f=open("demofile.txt","r")
print(f.read())




#dosyayı değiştirin başka şey yaz mesela

f=open("demofiles.txt","w")
f.write("woops ! ıhave deleted the content!")
f.close()

---------
f=open("demofiles.txt","r")
print(f.read())



# "x"‎ - Oluştur - bir dosya oluşturur, dosya varsa bir hata döndürür‎

# "a"‎ - Ekle - belirtilen dosya yoksa bir dosya oluşturur‎

# "w"‎ - Yaz - belirtilen dosya yoksa bir dosya oluşturur‎




#create a file called "myfile.txt"


f=open("myfile.txt","x")
#result : anew empty file is created

# ‎Bir dosyayı silmek için işletim sistemi modülünü almalı ve işlevini çalıştırmalısınız:‎os.remove()

import os 
os.remove("demofile.txt")

# Hata almamak için, dosyayı silmeye çalışmadan önce dosyanın var olup olmadığını denetlemek isteyebilirsiniz:‎

import os if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("the files does not exist")
    
# ‎Klasörün tamamını silmek için şu yöntemi kullanın:‎os.rmdir()    
    
    
import os #Note: You can only remove empty folders
os.rmdir("myfolder")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
‎


























    
