# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:19:02 2022

@author: Sümeyra Nihal GELMEZ
"""

# 1'den 10'a kadar olan sayıların on rastgele permütasyonunu üreten bir program yazın. 
# Rastgele bir permütasyon oluşturmak için, listedeki hiçbir girdinin aynı içeriğe sahip olmaması için 
# 1'den 10'a kadar sayılarla bir liste doldurmanız gerekir. Henüz listede olmayan bir değere sahip olana kadar rastgele değerler
#  oluşturarak kaba kuvvetle yapabilirsiniz. Ama bu verimsiz. Bunun yerine, bu algoritmayı izleyin. İkinci bir liste yapın ve 1'den 10'a 
#  kadar olan sayılarla doldurun. 10 kez tekrarlayın
# İkinci listeden rastgele bir öğe seçin.
# Kaldırın ve permütasyon listesine ekleyin.
import random
# produces one random permutation of the numbers 1 to 10 
def randomPermutation():
 secondList = []
 permutation = []
 # fill second list with numbers between 1 and 10 (inclusive)
 for i in range(1, 11):
 secondList.append(i)
 for i in range(10):
 # pick a random index in secondList
 randomIndex = random.randint(0, len(secondList) - 1)
 # find element at that index
 # and remove it from the secondList
 # notice: method pop() returns removed element
 randomElement = secondList.pop(randomIndex)
 # add that element to permutation list
 permutation.append(randomElement)
 print(permutation)
 
# 10 times calls a function
# since we need 10 permutations
for i in range(10):
 randomPermutation()
# Liste yapın ve 1'den 10'a kadar sayılarla doldurun.
# Bu liste boş olmasa da, içinden rastgele bir öğe seçin ve yeni listeye kaldırın.
# Bunu 10 kez tekrarlayın 