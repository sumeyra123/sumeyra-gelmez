# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:47:42 2022

@author: Sümeyra Nihal GELMEZ
"""

#♥Bir restorana gittiğinizde bahşiş hesaplamak zor değildir, ancak restoranınız dinleyicilerin aldığı hizmete göre bir bahşiş önermek ister. Aşağıdaki gibi lokantanın memnuniyetine göre bahşiş hesaplayan bir program yazın• * Bu derecelendirmeleri kullanarak lokantaların memnuniyet düzeyini sorun: 1 = Tamamen memnun, 2 = Memnun, 3 = Memnun değil.
#* Lokanta tamamen memnunsa, yüzde 20 bahşiş hesaplayın. * Lokanta memnunsa, yüzde 15 bahşiş hesaplayın. * Lokanta memnun değilse, yüzde 10 bahşiş hesaplayın.
#* Memnuniyet seviyesini rapor edin ve dolar ve sent cinsinden bahşiş verin.
price = float(input("Enter the dinner price: "))
satisfaction = int(input("Enter a diners' satisfaction (1 - totatally satisfied, 2 - satisfied, 3 - dissatifaction :"))
if satisfaction == 1:
 # tip is 20% of the diners' price 
 print("Totally satisfied! The tip is $" + str(price * 0.2))
elif satisfaction == 2:
 # tip is 15% of the diners' price
 print("Satisfied! The tip is$" + str(price * 0.15))
# input for satisfaction is 3
# since it's not 1 nor 2
else:
 # tip is 10% of the diners' price 
 print("Dissatisfied! The tip is $" + str(price * 0.1))