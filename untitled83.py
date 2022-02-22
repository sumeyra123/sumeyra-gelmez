# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:24:31 2022

@author: Sümeyra Nihal GELMEZ
"""
# Tiyatro oturma tablosu bilet fiyatları tablosu olarak şu şekilde uygulanır: 
#     10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
    
#     20 20 20 20 20 20 10 10 10 10 20 20 20 20 20 20 10 10 10 20 20 20 20 20 20 10 10 20 2
#     0 30 30 40 40 30 30 20 20 20 30 30 40 50 50 40 30 30 20 30 40 50 50 50 50 50 50 40 30
# Kullanıcılardan koltuk veya fiyat seçmelerini isteyen bir program yazın. Fiyatı 0 olarak değiştirerek satılan koltukları işaretleyin.
# Bir kullanıcı bir koltuk belirttiğinde, müsait olduğundan emin olun.
# Bir kullanıcı bir fiyat belirlediğinde, bu fiyata sahip herhangi bir koltuk bulun.
def pickBySeat(table, row, column):
 # suppose that user counts rows and columns from 1
 # so we need to decrease row and column
 row = row - 1
 column = column - 1
 # if this seat has price 0
 # it is already taken
 if table[row][column] == 0:
 print('Seat is already taken!')
 return table
 # else, set price to 0
 # and return a table
 else:
 table[row][column] = 0
 return table
 
def pickByPrice(table, price):
 # iterate over all elements in the table
for i in range(len(table)):

 for i in range(len(table)):
 for j in range(len(table[0])):
 # if there is element with value equals to price
 # reserve this seat (set price to 0)
 # and print message to user
 if table[i][j] == price:
 table[i][j] = 0
 print("You are reserve seat at " + str(i+1) + " row
 return table
 # if there isn't element with given price
 print("There are no seat with given price.")
 return table
table = [
 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
 [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
 [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
 [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
 [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
 [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
 [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]
pickBySeat(table, 1, 1)
pickByPrice(table, 50)

# İki fonksiyon yazın.
# İlk olarak girdilerle: tiyatro oturma çizelgeleri, aranan koltuk sırası ve sütunu.
# Ve girdileri olan ikinci fonksiyon: sinema salonu oturma planı ve bilet fiyatı.
# Bu işlev, tüm koltukları yineler ve verilen fiyatla ilkini rezerve eder.
# Bu fonksiyon bu koltuğun fiyatını bulur ve rezerve eder (fiyatı 0'a ayarlayın)
# koltuk müsaitse (fiyat != 0)