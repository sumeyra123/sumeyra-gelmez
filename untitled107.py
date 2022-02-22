# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:31:42 2022

@author: Sümeyra Nihal GELMEZ
"""

# İki kayan noktalı sayı sütunu içeren bir dosyayı okuyan bir program yazın.
#  Kullanıcıdan dosya adını isteyin. Her sütunun ortalamasını yazdırın.
import sys 
# if names of files are not entered in command line 
# prompt it from user
if len(sys.argv) < 2:
 inFilename = input("Enter a name of the first file: ")
 infile = open(inFilename, "r")
 outFilename = input("Enter a name of the second file: ")
 outfile = open(outFilename, "w")
# else read file names from list argv[]
else: 
 infile = open(sys.argv[1], "r")
 outfile = open(sys.argv[2], "w")
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