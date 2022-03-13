# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:13:40 2022

@author: Sümeyra Nihal GELMEZ
"""

import time
import vlc
G = vlc.MediaPlayer("C:/Users/Sümeyra Nihal GELMEZ/Downloads/mp3indirdur-Ibrahim-Tatlises-Dom-Dom-Kursunu-(Furkan-Demir-Remix).mp3")
G.play()
time.sleep(55)
G.stop()
#♠superclass
class Appointment:
    #every appointment has description
    def __init__(self,description):
        self.description=description
        #will be overridden in subclasses
        def occursOn(self,year,month,day):
            return
        #return description
        def getDescription(self):
            return self. _description
class OneTime(Appointment):
#we need all information: year,month and day
    def __init__(self,description,year,month,day):
        #call consructor from the superclass
        super().__init__(description)
        self._year=year
        self._month=month
        self._day=day
    def occursOn(self,year,month,day):
       if self._year == year and self._month == month and self._day==day:
           return True
       else:
            return False
class Daily (Appointment):
    def __init__(self,description):
        super(). __init__(description)
        #occurs everyday,so we just return true
    def occursOn(self,year,month,day):
            return True
            
class Monthly (Appointment):
    def __init__(self,description,day):
           super().__init__(description)
           self.__day=day
    #just compare days
    def occursOn(self,year,month,day):
        if self._day==day:
            return True
        else:
            return False
        

a1 = OneTime("dentist", 2019,8,1)
a2=Daily("gym")
a3 = Monthly("lunch - grandmother", 1)

appointment = [a1, a2, a3]

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
for a in appointment:
  if a.occursOn(year, month, day):
   print(a.getDescription())

  # Bir üst sınıf Randevusu ve Bir Kez, Günlük ve Aylık alt sınıfları 
  # uyguladım. Randevunun bir açıklaması (örneğin, "diş hekimine görün") 
  # ve bir tarihi vardır. Randevunun o tarihte gerçekleşip 
  # gerçekleşmediğini kontrol eden bir method createOn(yıl, ay, gün) 
  # yazdım. Örneğin, aylık bir randevu için ayın gününün eşleşip 
  # eşleşmediğini kontrol etmelisiniz. 
  # Ardından Randevu nesnelerinin bir listesini randevu 
  # karışımıyla doldurulmalı. Kullanıcının bir tarih girmesini ve o 
  # tarihte gerçekleşen tüm randevuları yazdırmasını sağlanmalıdır. 
# en üsstede müzik eşliğide dewam etmektedir .