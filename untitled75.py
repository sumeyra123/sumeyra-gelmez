# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:57:33 2022

@author: Sümeyra Nihal GELMEZ
"""

# Min işlevini veya remove yöntemini kullanmadan bir 
# listeden minimum değeri kaldıran bir removeMin işlevi yazın. 
def removeMin(values):
 minPos = 0
 minValue = values[0]
 pos = 1
 # iterate from second to last element
 while pos < len(values):
 # in each iteration update position of minimal element
 # and value of minimal element
 if values[pos] < minValue:
 minPos = pos
 minValue = values[pos]
 pos = pos + 1
 # after loop is completed
 # use pop(index) function to remove minimum value from the lis
 values.pop(minPos)
 
values = [3, 7, 2, 8]
removeMin(values) # prints [ 3, 7, 8]
values
# Listedeki tüm öğeleri yineleyin, her yinelemede minimum konum ve minimum değer güncelleyin.
# Sonunda, listeden minimum değeri kaldırmak için pop(index) yöntemini kullanın. 
