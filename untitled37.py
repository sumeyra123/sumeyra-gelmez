# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:08:01 2022

@author: Sümeyra Nihal GELMEZ
"""

#Write a program that translates a letter grade into a number grade. Letter grades are A, B, C, D, and F, possibly followed by + or –. Their numeric values are 4, 3, 2, 1, and 0. There is no F+ or F–. A + increases the numeric value by 0.3, a – decreases it by 0.3. However, an A+ has value 4.0.
#Enter a letter grade: B-
#The numeric value is 2.7.
grade = input("Enter a letter grade: ")
diff = 0
# if length of input is 2
# so there is "+" or "-" in grade
if len(grade) == 2:
 if grade[1] == "+":
diff = 0.3
 else:
 diff = -0.3
# every input is string
# so, in every case
# if it has length 2 or 1
# grade[0] letter grade (without + or -)
letter = grade[0]
# if grade is A we have only two possibilities
# if grade is A, we have only two possibilities 
# 4 or 3.7 (there is no 4.3)
if letter.upper() == "A" and diff == -0.3:
 print(4 + diff)
elif letter.upper() == "A":
 print(4)
# for grades B, C and D
# we need to add diff 
# depending on whether there was + or -
# diff would be positive or negative number (-0.3 or 0.3)
elif letter.upper() == "B":
 print(3 + diff)
elif letter.upper() == "C":
 print(2 + diff)
elif letter.upper() == "D":
 print(1 + diff)
# if grade is F and diff is not 0
# user writes F- or F+
# and there is no such grade
# so print "invalid input"
elif letter.upper() == "F" and diff != 0:
 print("Invalid input.")
else:
 print(0)