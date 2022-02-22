# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:33:14 2022

@author: Sümeyra Nihal GELMEZ
"""

# Komut satırında belirtilen tüm dosyaları arayan ve belirtilen bir kelimeyi içeren tüm satırları
#  yazdıran bir find.py programı yazın. Örneğin, eğer ararsanız
#  python find.py ring report.txt address.txt homework.py
#  then the program might print report.txt: has broken up an international ring of 
#  DVD bootleggers that address.txt: Kris Kringle, North Pole address.txt: Homer Simpson, Springfield
# homework.py: string = "text"
import sys
# returns -1 if there is no substring word in the file filename
# otherwise, returns line in which is given word 
def findLine(filename, word):
 # open a file
 infile = open(filename, "r")
 # read line 
 line = infile.readline()
 # while we are not at the end of the file
 while line != "": 
 # if there is a word, return current line
 # and close the file
 if word in line:
 infile.close()
 return line
 # read the next line
line = infile readline()

 # if there is no word in the file
 # close the file
 # and return -1
 infile.close()
 return -1
# given word from command line
word = sys.argv[1]
# iterate through given files
for i in range(2, len(sys.argv)):
 filename = sys.argv[i]
 if findLine(filename, word) != -1:
 # print result
 print(filename + ": " + findLine(filename, word))