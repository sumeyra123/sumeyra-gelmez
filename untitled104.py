# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:27:05 2022

@author: Sümeyra Nihal GELMEZ
"""

# Aşağıdaki görevleri yerine getiren bir program yazın:
#     Open a file with the name hello.txt.
#     Store the message “Hello, World!” in the file. 
#     Close the file.
#     Open the same file again.
#     Read the message into a string variable and print it.
# open a file with name "hello.txt"
outfile = open("hello.txt", "w")
# store the message "Hello, World!
outfile.write("Hello, World!")
# close the file
outfile.close()
# open the same file (but this time for reading)
infile = open("hello.txt", "r")
# read the message into a string variable
line = infile.read()
# print message 
print(line)
# close the file 
infile.close()