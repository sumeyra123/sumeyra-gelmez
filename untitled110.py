# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:42:10 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bir mağaza sahibi, günlük nakit işlemlerinin kaydını bir metin dosyasında tutar. 
# Her satırda üç öğe bulunur: Fatura numarası, nakit tutar ve tutar ödendiyse P harfi veya a
# lındıysa R harfi. Öğeler boşluklarla ayrılır. Mağaza sahibinden günün başındaki ve sonundaki 
# nakit miktarını ve dosyanın adını soran bir program yazınız. Programınız gerçek olup olmadığını
#  kontrol etmelidir.
# günün sonundaki nakit miktarı, beklenen değere eşittir.
# user inputs
filename = input("Enter a filename: ")
startAmount = float(input("Enter an amount at the beginning of the ))
endAmount = float(input("Enter an amount at the end of the day: "))
# open file
# raise error if file doesn't exist
try:
 inFile = open(filename, "r")
except IOError:
 raise IOError("The file doesn't exist.")
# read first line
line = inFile.readline()
while line != "":
 # remove "\n" from the end of the line
 line = line.rstrip()
 # split with delimiter " "

 line = line.split()
 # if in third column is "R" add second column to startAmount
 if line[2] == "R":
 startAmount = startAmount + float(line[1])
 # elif if in third column is "P", subtract second column from 
 elif line[2] == "P":
 startAmount = startAmount - float(line[1])
 # read the next line
 line = inFile.readline()
# print result 
if startAmount == endAmount:
 print("Ok")
else:
 print("Not ok")
# close the file
inFile.close()