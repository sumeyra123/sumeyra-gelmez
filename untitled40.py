# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:14:56 2022

@author: Sümeyra Nihal GELMEZ
"""

# Write a program that prompts the user to provide a single character from the alpha­ bet. Print Vowel or Consonant, depending on the user input. If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error
#message
userInput = input("Enter a letter: ")
# if length of input is not 1
# or if input is not letter
# print an error message 
if len(userInput) != 1 or not userInput.isalpha():
 print("Invalid input.")
 
# if input is some of the 
# letters in set {A, E, I, O, U}
# it's a vowel
# notice: it's a shorter syntax for
# if input == "A" or input == "E" or ... or input == "U"
if userInput.upper() in {"A", "E", "I", "O", "U"}:
 print("Vowel")
# otherwise, it's a consonant
else:
    print("Consonant")