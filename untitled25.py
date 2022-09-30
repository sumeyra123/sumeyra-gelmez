# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:41:55 2022

@author: Sümeyra Nihal GELMEZ
"""

#nesne tabanlı programlama
# Nesne tabanlı programlama, komut arayüzlü programlar geliştirmek için de kullanışlı bir programlama
#yöntemidir.Peki tam olarak nedir bu sınıf denen şey? Çok kaba ve oldukça soyut bir şekilde tanımlayacak olursak, sınıflar, nesne üretmemizi sağlayan veri tipleridir. İşte nesne tabanlı programlama, adından da anlaşılacağı gibi, nesneler
#(ve dolayısıyla sınıflar) temel alınarak gerçekleştirilen bir programlama faaliyetidir.
#Diyelim ki, kullanıcının girdiği bir kelimedeki sesli harfleri sayan bir kod yazmak istiyorsunuz. Bu amacı gerçekleştirebilmek için yazabileceğiniz en basit kod herhalde şu olacaktır:
"""
sesli_harfler ='aeıioöuü'
sayaç=0
kelime=input ('bir kelime girin:')
for harf in kelime:
    if harf in sesli_harfler:
        sayaç+=1
mesaj='{} kelimesinde {} sesli harf var'
print(mesaj.format(kelime,sayaç)) 
"""
# sesli_harfler ='aeıioöuü'
# sayaç=0
# kelime=input ('bir kelime girin:')
# def seslidir (harf):
#     return harf in sesli_harfler
# def arttır():   
#     global sayaç 
#     for harf in kelime: 
#       if seslidir(harf):
#             sayaç+=1
#     return sayaç
# mesaj='{} kelimesinde {} sesli harf var '
# print(mesaj.format(kelime,arttır()))     

#boş bir sınıf tanımlama 
# class Çalışan ():
#      pass
 #çalışana sınıfı oluşturmak istiyorumve ve sınıf tanımlayıp kabiliyetlerini yazacağım.
# class Çalışan ():
#     kabiliyetleri =[]#Burada unvanı ve kabiliyetleri adlı iki #değişken tanımladık. Teknik dilde bu değişkenlere ‘sınıf niteliği’ (class attribute) adı verilir.
#     unvanı ='işçi'
# print(Çalışan.kabiliyetleri)
# print(Çalışan.unvanı)#Bildiğiniz gibi, bir fonksiyonu tanımladıktan sonra, o fonksiyonun işlemeye başlaması için, o fonksiyonun mutlaka çağrılması gerekir.
#Çağrılmayan fonksiyonlar çalışmaz. 
# Burada Çalışan() adlı sınıfın niteliklerine nasıl 
# eriştiğimize dikkat edin. Gördüğünüz gibi, 
# sınıf niteliklerine erişmek için doğrudan sınıfın adını 
# parantezsiz bir şekilde kullanıyoruz. 
# Eğer sınıf adlarını parantezli bir şekilde yazarsak başka 
# bir şey yapmış oluruz. Bundan biraz sonra bahsedeceğiz. 
# Biz şimdilik, sınıf niteliklerine erişmek için sınıf 
# adlarını parantezsiz
# kullanmamız gerektiğini bilelim yeter.
# Gelin isterseniz yukarıdaki Çalışan() sınıfına birkaç nitelik
 # daha ekleyerek bu iddiamızı destekleyelim:
# class Çalışan():
#      kabiliyetleri=[]
#      unvanı='işçi'
#      memleketi=''
#      doğum_tarihi=''
# Burada belli kabiliyetleri, unvanı, maaşı, memleketi 
# ve doğum_tarihi olan bir Çalışan() sınıfı tanımladık. 
# Yani ‘Çalışan’ adlı bir grubun ortak niteliklerini belirledik. 
# Elbette her çalışanın memleketi ve doğum tarihi farklı olacağı 
# için sınıf içinde bu değişkenlere belli bir değer atamadık. 
# Bunların birer karakter dizisi olacağını 
# belirten bir işaret olması için yalnızca
# memleketi ve doğum_tarihi adlı birer boş karakter dizisi tanımladık.    

# sınıf niteliklerine, doğrudan sınıf adını kullanarak erişebileceğimizi biliyorsunuz

# print(Çalışan.kabiliyetleri)
# print(Çalışan.unvanı)
# print(Çalışan.memleketi)

# class Çalışan():
#      kabiliyetleri=[]
#      unvanı='işçi'
#      memleketi=''
#      doğum_tarihi=''
#      maaşı='1500'
# ahmet=Çalışan()
# Burada sınıfımızı ahmet adlı bir değişkene atadık. 
# İşte bu işleme teknik dilde ‘örnekleme’ veya ‘örneklendirme’ 
# (instantiation) adı verilir. Bu işlemi fonksiyon çağırma 
# ile kıyaslayabiliriz: Python programlama dilinde bir fonksiyonu 
# ullanışlı hale getirme işlemine ‘çağırma’, bir sınıfı kullanışlı
#  hale getirme işlemine ise ‘örnekleme’ adı
# veriyoruz.
#♣ asker sınıfı oluşturalım
# class Asker ():
#     rütbesi ='er'
#     standart_techizat=['el bommbası ,tüfek ,bıçak,çadır']
#     gücü='60'
#     birliği=''
# Asker.rütbesi
# Asker.standart_techizat
# Asker.gücü
# Asker.birliği    
# mehmet=Asker()İşte, teknik olarak ifade etmemiz gerekirse, sınıfları bir isme atama işlemine örnekleme (veya örneklendirme) adı veriyoruz.

# class Sipariş ():
#     firma =''
#     miktar=0
#     sipariş_tarihi=''
#     teslim_tarihi=''
#     stok_adedi=0
# jilet =Sipariş()#Sınıfın gövdesinde tanımladığımız şu değişkenler birer sınıf niteliğidir (class attribute):
# jilet = Sipariş() komutunu verdiğimizde ise, biraz 
# önce tanımladığımız sınıfı örnekleyip (instantiation), 
# bunu jilet adlı bir örneğe (instance) atamış oluyoruz. 
# Yani jilet, Sipariş() adlı
# sınıfın bir örneği olmuş oluyor. 
# 
# kalem =Sipariş ()
# pergel=Sipariş()
# silgi=Sipariş()

# from sipariş import Sipariş


class Çalışan(): 
    kabiliyetleri = [] 
    unvanı = ' işçi' 
    maaşı = 1500 
    memleketi = ' '
    doğum_tarihi = ' '
ahmet = Çalışan()
mehmet = Çalışan()
ayşe = Çalışan()    
print(ahmet. kabiliyetleri)
print(ahmet. unvanı)

print(mehmet. maaşı) 
print(mehmet. memleketi)

print(ayşe. kabiliyetleri)
print(ayşe. doğum_tarihi)
ahmet.kabiliyetleri.append('bodyguard')
ahmet=Çalışan()
print(ahmet.kabiliyetleri)
# Şimdi Çalışan() sınıfının bir başka örneğini oluşturalım:
selim=Çalışan()
selim.kabiliyetleri.append('yüzme')
print(selim.kabiliyetleri)
# ****///__init__ Fonksiyonu ve self







 