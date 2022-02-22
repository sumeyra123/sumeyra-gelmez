# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:58:04 2022

@author: Sümeyra Nihal GELMEZ
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 17:49:17 2022

@author: Sümeyra Nihal GELMEZ


#1-100 Arası Sayıları Ekranda Listeleyen Python kodunu yazınız
for i in range (1,100):
    print (i)
"""    
#    1-100 Arası Sayıları Ekranda  çift Listeleyen Python kodunu yazınız
for i in range (1,101):
    if i %2==0:
       print(i)
#1- 100 arasındakı tek sayılar yaz
for  i in range (1,101):
    if i%2!=0:
        print(i)
# 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python kodunu yazınız.
for  i in range (1,101):
    if i%3==0 and i %5==0:
        print(i)
#1 den başlayıp Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python kodunu yazınız.
a=int(input("please enter your munber:"))
for i in range(a):
     print (i)
#Girilen metnin harflerini alt alta yazdıran Python kodunu yazınız.
name=input("please enter your name:")
for  i in  (name):
   name+=name
   print (" ı spelled my name",i)
#Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python kodunu yazınız
total=0
a=int(input("pleaes enter your number:"))
b=int(input("please enter your 2.number :"))
for i in range (a,b):
   total =total+i
print("total:="),total
#Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan gösteren Python kodunu yazınız.
value=0
a=int(input("please enter your number:"))
for  i in range (2,a):
     if a%i==0:
         value+=1
         break
if value!=0:
         print("not prime number")
else:
         print("prıme number")
#1 den başlayarak kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren Python ko         
 number = int(input('Enter the Number : '))

oddtotal=0
doubletotal=0
for i in range(1,number):
  if(i%2==0):
    doubletotal+=i
else:
    oddtotal+=i
print("Sum of Odd Numbers:"+ str (oddtotal))
print("Sum of Even Numbers:"+str(doubletotal))
#Python ile bir liste içinde 5’in katları olan sayıları listeleme.
for  i in range (5,90):
    if i%5==0:
     print("Number =" + str (i)+"- the square of the number ="+ str (i**2))         