# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:20:36 2022

@author: Sümeyra Nihal GELMEZ
"""
# Sihirli kareler. 1, 2, 3, sayılarıyla dolu bir n × n matrisi. . ., n2, her satırdaki, 
# her sütundaki ve iki köşegendeki öğelerin toplamı aynı değerdeyse sihirli bir karedir. 
# Klavyeden 16 değeri okuyan ve 4×4 tabloya konulduğunda sihirli kare oluşturup oluşturmadığını test eden bir program yazın. 
# İki özelliği test etmeniz gerekiyor: 1. Kullanıcı girişinde 1, 2, …, 16 sayılarının her biri var mı? 2. Sayılar bir kareye konulduğunda satır, 
# sütun ve köşegenlerin toplamları birbirine eşit midir?
def magicSquares(values):
 # check if there is all values from 1 to 16
 for i in range(1, 17):
 if i not in values:
 return False 
 # put values in 4*4 table
 pos = 0
 table = []
 for i in range(4): 
 row = []
 for j in range(4):
 row.append(values[pos])
 pos = pos + 1
 table.append(row)
 
 # calculate sum of first row
 sum = table[0][0] + table[0][1] + table[0][2] + table[0][3]
 
# check if sums of all rows are equal to sum

 # check if sums of all rows are equal to sum
 if not checkRows(table, sum):
 return False
 # check if sums of all columns are equal to sum
 if not checkColumns(table, sum):
 return False
 # check if sums of both diagonals are equal to sum 
 if not checkDiagonals(table, sum):
 return False
 # if function does not return False yet
 # table is magic square
 # and return True 
 return True
def checkRows(table, sum):
 for i in range(4):
 sumRow = 0
 for j in range(4):
 sumRow = sumRow + table[i][j]
 if sumRow != sum:
 return False
 return True
def checkColumns(table, sum):
 for j in range(4):
 sumColumn = 0
 for i in range(4):
 sumColumn = sumColumn + table[i][j]
 if sumColumn != sum:
 return False
 return True
def checkDiagonals(table, sum):
 diagonal1 = 0
 diagonal2 = 0
 
 for i in range(4):
 for j in range(4):
 # elements on second diagonal are on indexes 
 # [0][3], [1][2], [2][1], [3][0]
 if i + j == 3:
 diagonal2 = diagonal2 + table[i][j]
 # elements on first diagonal are on indexes
 # [0][0], [1][1], [2][2], [3][3]

 if i == j:
 diagonal1 = diagonal1 + table[i][j]
 if diagonal2 != sum or diagonal1 != sum:
 return False
 return True
 
# user input
values = []
for i in range(16):
 num = int(input("Enter a number between 1 and 16:"))
 values.append(num)
 
magicSquares(values)
# 4 fonksiyon yazın.
# Satırların toplamının verilen sayıya eşit olup olmadığını kontrol eden.
# Sütunların toplamının verilen sayıya eşit olup olmadığını kontrol eden.
# Köşegenlerin toplamının verilen sayıya eşit olup olmadığını kontrol eden.
# giriş listesinde 1'den 16'ya kadar tüm değerlerin olup olmadığını kontrol eder.
# Ve diğer işlevleri çağıran, verilen girdi listesinden tablo yapar, 
