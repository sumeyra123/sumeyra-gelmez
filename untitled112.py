# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:56:10 2022

@author: Sümeyra Nihal GELMEZ
"""

# Üç dosyadan bilgi sorgulayan bir program yazın. İlk dosya, bir grup insanın isimlerini 
# ve telefon numaralarını içerir. İkinci dosya, bir grup insanın adlarını ve Sosyal 
# Güvenlik numaralarını içerir. Üçüncü dosya, bir grup insanın Sosyal Güvenlik 
# numaralarını ve yıllık gelirini içerir. İnsan grupları örtüşmelidir, ancak tamamen aynı 
# olması gerekmez. Programınız kullanıcıdan bir telefon numarası istemeli ve ardından adı, 
# Sosyal Güvenlik numarasını yazdırmalıdır.
# ber, ve yıllık gelir, eğer bu bilgileri belirleyebilir.
# returns name with corresponding telephone number from file1, if 
# otherwise returns -1
def getName(telNum, file1):
 line = file1.readline()
 while line != "":
 # remove "\n" from the end of line
 line = line.rstrip()
 # notice: name can contain " "
 line = line.rsplit(" ", 1)
 if line[1] == telNum:
 return line[0]
 # read the next line
 line = file1.readline()
 return -1
# the logic is the same for other two functions
def getSocSecNum(name, file2):
 line = file2.readline()
while line != "":

 while line != :
 line = line.rstrip()
 line = line.rsplit(" ", 1)
 if line[0] == name:
 return line[1]
 line = file2.readline()
 return -1
def getIncome(socSecNum, file3):
 line = file3.readline()
 while line != "":
 line = line.rstrip()
 line = line.rsplit(" ", 1)
 if line[0] == socSecNum:
 return line[1]
 line = file3.readline()
 return -1
# user inputs
filename1 = input("Enter a first filename: ")
filename2 = input("Enter a second filename: ")
filename3 = input("Enter a third filename: ")
# open files 
file1 = open(filename1, "r")
file2 = open(filename2, "r")
file3 = open(filename3, "r")
# user enters telephone number
telNum = input("Enter a telephone number: ")
# get name from telNum in file1
name = getName(telNum, file1)
# if there is a name
if name != -1:
 # print it
 print("Name: " + name)
 # get a social secure number from name in file2
 socSecNum = getSocSecNum(name, file2)
 # if there is a social secure number 
 if socSecNum != -1:
 # print it
 print("Social secure number: " + socSecNum)
 # and try to find annual income using social secure number 
Egzersiz 26 Egzersiz 28
 income = getIncome(socSecNum, file3)
 # if there it is
 if income != -1:
 # print it
 print("Annual income: " + income)
# close files
file1.close()
file2.close()
file3.close()