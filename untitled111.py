# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:43:45 2022

@author: Sümeyra Nihal GELMEZ
"""

# Aşağıdaki formatta bir metin dosyasından  birden fazla 
# öğrencinin sınav notlarını okuyan bir program yazınız,
# Luigi
# 80 69 75
# Dikenli
# 85 89 92
# sakızlı
# 78 87 82
# Arthur 89 94 91
# ve burada gösterilen elektronik tabloyu oluşturmak için kullanılabilecek bir CSV dosyası oluşturur.
from csv import writer
# Open the text and csv files
filename = input("Enter a name of txt file: ")
txtFile = open(filename, "r")
csvFile = open("new.csv", "w")
csvWriter = writer(csvFile)
# Add first three rows in the new csv file
csvWriter.writerow(["Basket Weaving 101"])
csvWriter.writerow([""])
csvWriter.writerow(["Student", "Exam1", "Exam2", "Exam3", "Average"])
# read textFile line by line
line = txtFile.readline()
while line != "":
 # we now that the name is first written
 name = line.rstrip()


 # read line with results 
 line = txtFile.readline()
 # remove "\n" from the end
 line = line.rstrip()
 # make list of words
 line = line.split()
 # calculate average of all three numbers
 average = (int(line[0]) + int(line[1]) + int(line[2])) / 3
 # write a row 
 newRow = [name, line[0], line[1], line[2], round(average, 2)]
 csvWriter.writerow(newRow)
 # read the next line
 line = txtFile.readline()
# close files 
txtFile.close()
csvFile.close() 