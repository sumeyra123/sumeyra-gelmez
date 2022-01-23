# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:12:24 2022

@author: Sümeyra Nihal GELMEZ
"""

#Write a program that takes user input describing a playing card in the following shorthand notation: 
card = input("Enter a card notation: ")
# card is string with length 2 
# or 3 (only if the value is 10)
# if length is 2
# first character is value 
if len(card) == 2:
 value = card[0]
 # and second character is sign of the card
 sign = card[1] 
# and if length is 3
# first two characters are value
else:
 value = card[:2]
 # and third is sign
 sign = card[2]
 
if value.upper() == "A":
 output = "Ace "
elif value.upper() == "J":
 output = "Jack "
elif value.upper() == "Q":
 output = "Queen "
elif value.upper() == "K":
 output = "King "
# card value is 2, 3, ..., or 10
else:
 output = value + " "
 
# concatenate the sign of card
if sign.upper() == "D":
 output += "of Diamonds"
elif sign.upper() == "H":
 output += "of Hearts"
elif sign.upper() == "S":
 output += "of Spades"
else:
 output += "of Clubs"
 
# print an output 
print(output)    