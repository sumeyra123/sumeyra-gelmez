# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:14:20 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bir listede 20 rastgele kalıp atma dizisi oluşturan ve kalıp değerlerini yazdıran, 
# yalnızca en uzun çalışmayı işaretleyen 
# bir program yazın: 1 2 5 5 3 1 2 4 3 (2 2 2 2) 3 6 5 5 6 3 1
# Birden fazla maksimum uzunlukta koşu varsa, ilkini işaretleyin. 
def markLongestRun(values):
 # function findLongestRun returns 
 # length of the longest run
 # and index after last element in this run 
 length, stop = findLongestRun(values)
 # start is first index in the run
 start = stop - length 
 for i in range(len(values)):
  if i == start:
   print("( ", end = "")
 # run is over, print )
  elif i == stop:
   print(") ", end = "")
   print(str(values[i]) + " ", end = "")
 # if few last elements are in the longest run
 # stop will never become i in for loop
 # so it is a special case
 if stop == len(values):
    print(")")
 
def findLongestRun(values):
 inRun = False
 length = 1
 maxLength = 0
 stop = 1
 i = 0
 # from first to second last element 
 while i < len(values) - 1:
   if values[i] == values[i + 1]:
    inRun = True
 length = 1
 # while we are in run and while we are in the legal in
 while inRun and i < len(values) - 1:
  if values[i] == values[i + 1]:
 # increment length 
    length = length + 1
 # and go to the next element
 i = i + 1
 # current run is over 
 # update maxLength and stop
 # set inRun to False
 # and go to the next element
else: 
if length > maxLength:
 maxLength = length
 stop = i + 1
 inRun = False
 i = i + 1
 # if loop is over and we are still in run
 # last few elements are in the run
 # so you need update maxLength and stop 
 if inRun:
 if length > maxLength:
 maxLength = length
 stop = i
 return maxLength, stop
 
 
values = []
# generate a sequence of 20 random die tosses 
for i in range(20):
 num = random.randint(1, 6)
Egzersiz 15 Egzersiz 17
 values.append(num)
print(values)
 
markLongestRun(values)