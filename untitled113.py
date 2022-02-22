# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:00:32 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bir otel satış elemanı, satışları bir metin dosyasına girer. 
# Her satır, noktalı virgülle ayrılmış olarak aşağıdakileri içerir:
#     Müşterinin adı, satılan hizmet (Akşam Yemeği, Konferans, Konaklama vb.), s
#     atış tutarı ve bu etkinliğin tarihi. Böyle bir dosyayı okuyan ve her hizmet için toplam tutarı 
#     gösteren bir program yazın.
# kategori. Dosya yoksa veya biçim yanlışsa bir hata görüntüler.
import re
# checks if format is correct
def validate(line):
 # [A-Za-z\s]+ -> name of client 
 # [A-Za-z]+ -> service sold
 # [0-9]+ -> amount of sale
 # [0-9]+[/][0-9]+[/][0-9]+ -> date
 pattern = re.compile("^[A-Za-z\s]+[:][A-Za-z]+[:][0-9]+[:][0-9]")
 if pattern.match(line):
 return True
 else:
 return False
# user input
filename = input("Enter a filename: ")
# open file


# raise error if file doesn t exist
try:
 inFile = open(filename, "r")
except IOError:
 raise IOError("The file doesn't exist.")
# initialize sericeList and servicePrice 
serviceList = []
servicePrice = []
# read first line
line = inFile.readline()
while line != "":
 # if format isn't correct raise error
 if validate(line) == False:
 raise ValueError("Incorrect format!")
 # remove "\n" from the end of the line
 line = line.rstrip()
 # split with delimiter ":"
 line = line.split(":")
 # if service name is not in the serviceList add it
 # and add price to the servicePrice list
 if line[1] not in serviceList:
 serviceList.append(line[1])
 servicePrice.append(int(line[2]))
 # if service name is already in the list
 # just add price to the corresponding element in the servicePr
 else:
 pos = serviceList.index(line[1])
 servicePrice[pos] = servicePrice[pos] + int(line[2])
 # read the next file
 line = inFile.readline()
# print result 
for i in range(len(serviceList)):
 print(serviceList[i] + ": " + str(servicePrice[i]))
# close the file
inFile.close()