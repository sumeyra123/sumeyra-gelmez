# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:09:36 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bir çalıştırma, bitişik tekrarlanan değerlerin bir dizisidir. 
# Bir listede 20 rastgele kalıp atma dizisi oluşturan ve kalıp değerlerini yazdıran, sayıları parantez 
# içine alarak işaretleyen bir program yazın: 1 2 (5 5) 3 1 2 4 3 (2 2 2 2 ) 3 6 (5 5) 6 3 1
# Aşağıdaki sözde kodu kullanın: inRun bir boole değişkenini false olarak ayarlayın. Listedeki her geçerli dizin için i if inRun
# [i] değerleri önceki Print ) değerinden farklıysa. inRun = yanlış.
# Run değilse
# Değerler[i] aşağıdaki Print (.inRun = true.
# Değerleri yazdır[i]. inRun ise, yazdırın). 
def markRuns(values):
 inRun = False
 for i in range(len(values)):
 # if we are in run 
    if inRun:
 # and current element is different from the preceding 
 # we need to close run with )
 # and set inRun to False
if values[i] != values[i - 1]:
 print(") ", end = "")
 inRun = False
 # if we are not in run and current element is not last
 if not inRun and i != len(values) -1:
 # and if the following element is the same as current
 # we need to start new run
 # print ( and set inRun to True
 if values[i] == values[i + 1]:
 print("( ", end = "")

 inRun = True
 # in every case, we print current element
 print(str(values[i]) + " ", end = "")
 # if loop is completed and we are still in run
 # it means that the last element is in run
 # and we need to close run with ) 
 if inRun:
 print(")", end = "")
values = []
# generates a sequence of 20 random die tosses 
for i in range(20):
 num = random.randint(1, 6)
 values.append(num)
 
markRuns(values)
