# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:29:08 2022

@author: Sümeyra Nihal GELMEZ
"""

# Metin içeren bir dosyayı okuyan bir program yazın.
# Her satırı okuyun ve satır numaralarından önce çıktı dosyasına gönderin. giriş dosyası ise
# open a files
inFilename = input("Enter a name of the first file: ")
infile = open(inFilename, "r")
outFilename = input("Enter a name of the second file: ")
outfile = open(outFilename, "w")
# counts lines in the first file
counter = 1
# read the line into a string variable
line = infile.readline()
# while we are not at the end of the file
while line != "": 
 # write in the second file
 outfile.write("/* " + str(counter) + " */ " + line)
 # read next line
 line = infile.readline()
 # increment counter
 counter = counter + 1
# close the files
outfile.close()
infile.close()
