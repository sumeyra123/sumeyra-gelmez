# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:55:26 2022

@author: Sümeyra Nihal GELMEZ
"""
import ctypes
import sys
class DynamicArray(object):
    def __init__(self):
        
        self.size = 0  #üç değişken yaratırız, nesne boyutu .size yani dizinin gerçek alanı veya geçerli uzunluğu
       
        self.capacity = 1   #  self.array bu dizi değişkeni, dizimiz için gerçek dizi öğelerini tutuyor.
        self.array = self._create_array(self.capacity)#dizi için sahip olabileceğimiz maksimum boyut olan kapasite anlamına gelir.
    
    def __len__(self): #dizinin uzunluğunu yakalamak için kullanabileceğimiz bu yöntem.
        
        return self.size

    def __getitem__(self, index): #bu yöntem, dizi öğelerini dizinlere göre kullanabiliriz.İndexle ulaşiyoruz.
      
        if not 0 <= index <self.size: ## dizininin dizi sınırları içinde olup olmadığını kontrol eder.
            raise IndexError('Given index: {0} is larger than array size {1}'.format(index, self.size))

        return self.array[index]
    
    def _create_array(self, length):
        
      
        return [None] * length

    def _resize(self, new_capacity): #re_size işlevinin yaptığı şey, yeni bir kapasiteye sahip yeni bir dizi oluşturmak ve ardından eski dizideki öğeleri yeni diziye kopyalamak 
     #ve son olarak mevcut dinamik dizimizi temsil etmek için yeni bir dizi kullanmak 
       
        new_array = self._create_array(new_capacity)

        #
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, element): #bu ekleme yöntemi, dizimize yeni öğeler eklemek için bir kullanımdır, mevcut dizimiz kapasiteye ulaştığında, kapasiteyi ikiye katlamak için mevcut dizimizi yeniden boyutlandıracağız.
        
        if self.size == self.capacity:
            self._resize(2 * self.capacity) #, kapasiteyi ikiye katlamak için mevcut dizimizi yeniden boyutlandıracağız.

        self.array[self.size] = element
        self.size += 1
       
    def extend(self, size): #güncelleme yaptim burda diziye ulaşıp ekelmek için yanlişda olabilir hocam bilmiyorum.
      
        for element in size:
            self.append(element)

      def insert(self,element ):  #buradada ekledim yeni elemente
       
        if self._lenght == self._capacity:  
            self._capacity
     
    def pop(self):  #. Öğeyi dizinin sonundan çıkarmak için kullandığımız bir yöntem, böylece dizinin son öğesini basitçe atamak için ne yapar. burada yaptığımız şey, dizinin mevcut uzunluğu 
    #kapasitenin 4'ünden azsa, kapasitemizi mevcut kapasitenin yarısına yeniden boyutlandıracağız, 
    #bu mantığın nedeni, kapasitenin yarısına yeniden boyutlandırarak dizimiz tüketecektir. daha az hafıza demektir
        
        element = None
        
        if self.size > 0:
            element = self.array[self.size - 1]
            self.array[self.size - 1] = None
            self.size -= 1
        
            if self.size <= self.capacity // 4:
                self._resize(self.capacity // 2)
            
        return element
# # neden 2 yerine 4'ü buraya böldüğünü sorabilir, başka bir örnek verelim, diyelim ki kapasite dizimiz ve 
# 1 boyutumuz var, bu yüzden şimdi bu dizi kullanacak 2 hafıza diyelim, burada 2'ye bölünürsek ve şimdi bu mantıktan sonra,
#  boyut 1 ve kapasite 1'den oluşan bir dizimiz olacak, yani 2 burada bir hafıza kullanıyor yani bunun 
#  dezavantajı, eğer başka bir tane varsa ne olur? bundan sonra işlem ekle ilk durumda, eğer başka bir eklersek, diziye 1. sıradaki 
#  işlemi alan yeni bir eleman ekleriz ve ikinci durumda, diziyi 2 kapasitesine ve bir kopya1'i yeni diziye yeniden boyutlandırmamız gerekir ve 
#  eklemeyi yapılır, bu nedenle genellikle re_size işlemi kopyalandığından beri eski dizideki öğeleri yeni diziye yerleştirmek
#  genellikle n düzeyindedir, bu nedenle bu şekilde sonraki ekleme ve n sırasına mal olur, ancak ilk yöntem, aşağıdaki eklemenin maliyeti 
#  1'dir ve eğer bir eklememiz varsa ve 4'e bölünen ilk yöntemleri kullanan eşit olasılıklara sahip bir pop her zaman daha iyidir.