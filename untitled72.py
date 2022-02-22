# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:44:42 2022

@author: Sümeyra Nihal GELMEZ
"""

#P6.4 Bir tamsayı listesi için aşağıdaki görevleri yerine getiren liste işlevlerini yazın. 
#Her fonksiyon için bir test programı sağlayın. a. Listedeki ilk ve son öğeleri değiştirin. 
#B. Tüm öğeleri birer birer sağa kaydırın ve son öğeyi ilk konuma taşıyın. Örneğin, 1 4 9 16 25, 25 1 4 9 16'ya dönüştürülür.
#C. Tüm çift öğeleri 0 ile değiştirin. d. İlk ve sonuncu hariç her bir elemanı iki komşusundan daha büyük olanıyla değiştirin. 
#e. Liste uzunluğu tek ise ortadaki öğeyi, uzunluk çift ise ortadaki iki öğeyi kaldırın.
#F. Tüm çift öğeleri öne doğru hareket ettirin, aksi takdirde öğelerin sırasını koruyun.
# G. Listedeki en büyük ikinci öğeyi döndür. H. Liste şu anda artan düzende sıralanmışsa true değerini döndürün.
# Bence. Liste iki bitişik yinelenen öğe içeriyorsa true değerini döndürün.
# J. Liste yinelenen öğeler içeriyorsa (bunların bitişik olması gerekmez) true değerini döndürün. 

# a. 
def swapFirstLast(values):
 # temp now has value of first element
 temp = values[0]
 # first element now has value of last element
 values[0] = values[len(values)-1]
 # and last element has value of temp 
 # (how has value of first element)
 values[len(values)-1] = temp
values = [ 1, 2, 3, 4, 5]
swapFirstLast(values)
values # prints [ 5, 2, 3, 4, 1]
# b. 
def shiftRight(values):
# save value of last element in temp
temp = values[len(values)-1]
# iterate over all elements between second last and first

for i in range (len(values)-2, -1, -1):
# and shift it by one to the right
values[i+1] = values[i]
# after loop is completed
# give first element value of last element
values[0] = temp
values = [1, 4, 9, 16, 25]
shiftRight(values)
values # prints [ 25, 1, 4, 9, 16]
# c. 
def replaceEven(values):
for i in range(len(values)):
# if remainder after division values[i] by 2 is zero
# values[i] is even number
# so give it value 0 
if values[i] % 2 == 0:
values[i] = 0
values = [1, 2, 3, 4, 5]
replaceEven(values)
values # prints [1, 0, 3, 0, 5]
# d. 
def replaceWithNeighbor(values):
# iterate over all elements without first and last
for i in range(1, len(values)-1):
# find maximum of two neighbors
new = max(values[i-1], values[i+1])
# and give new value to current element
values[i] = new
values = [1, 6, 3, 4, 5, 2, 8, 5]
replaceWithNeighbor(values)
values # prints [1, 3, 4, 5, 5, 8, 8, 5]
# e. 
def removeMiddle(values):
# if length is even we need to remove two elements
# if length is even we need to remove two elements
if len(values) % 2 == 0:
# operation // is floor division
# removing first (left) of these two 
values.pop(len(values) // 2)
# removing second (right) of these two
values.pop(len(values) // 2)
else:
# removing the middle element
values.pop(len(values) // 2)
values1 = [1, 6, 3, 4, 5, 2, 8, 5]
removeMiddle(values1)
print(values1) # prints [1, 6, 3, 2, 8, 5]
values2 = [1, 6, 3, 4, 5, 2, 8, 5, 10]
removeMiddle(values2) # prints [1, 6, 3, 4, 2, 8, 5, 10]
print(values2)
# f. 
def moveEven(values):
for i in range(len(values)):
# if current element is even
if values[i] % 2 == 0:
# remove it from the list
temp = values.pop(i)
# and insert at first position
values.insert(0, temp)
values = [1, 6, 3, 4, 5, 2, 8, 5]
moveEven(values) # prints [8, 2, 4, 6, 1, 3, 5, 5]
values
# g. 
def secondLargest(values):
# first sort given list
values.sort()
# we know that maximal element is on the last position
max1 = values[len(values)-1]
found = False
i = len(values) - 2
# if we have a list with more than one maximal elements
# second largest will not be at the second last position
# second largest will not be at the second last position
# so we are finding first different from largest backwards
# iterate over all elements from the second last to the first
while i > -1 and not found:
if values[i] != max1:
max2 = values[i]
found = True
i = i - 1
return max2
values = [1, 6, 3, 4, 5, 2, 8, 5]
secondLargest(values) # prints 6
# h. 
def isSorted(values):
# iterate over all elements from first to second last 
# notice: i can't be last index, 
# since in the loop we are using values[i+1]
# if i goes from first to last index
# we will get error (index out of range)
for i in range(len(values)-1):
if values[i] > values[i+1]:
return False
# if loop is completed, it must be 
# values[i] <= values[i+1] for all i
# it means that list is sorted in increasing order
return True
values1 = [1, 3, 4, 5, 8]
print(isSorted(values1)) # prints True
values2 = [1, 5, 3, 4, 5, 8]
print(isSorted(values2)) # prints False
# i. 
def adjacentDuplicate(values):
# i can't be last index 
# because in the loop we are using values[i+1]
for i in range(len(values)-1):
# if there are a equal adjacent elements return True
if values[i] == values[i+1]:
return True
# if l i l t d it t b
# if loop is completed, it must be 
# values[i] != values[i+1] for all i
# it means that there are not equal adjacent elements 
return False
values1 = [1, 3, 4, 5, 8]
print(adjacentDuplicate(values1)) # prints False
values2 = [1, 5, 3, 4, 5, 5]
print(adjacentDuplicate(values2)) # prints True
# j. 
def duplicate(values):
# iterate over all elements
for i in range(len(values)):
# save current element in variable num
num = values[i]
# again iterate over all elements
for j in range(len(values)):
# and if you find element with same value as num 
# but with different position
# there are duplicate elements in the list
if i != j and values[i] == values[j]:
return True
# if the loop is completed,
# there are no duplicate elements in the list
return False
values1 = [1, 3, 4, 5, 8]
print(duplicate(values1)) # prints False
values2 = [1, 3, 4, 5, 3]
print(duplicate(values2)) # prints True
# #a) Kitaptaki örnekte olduğu gibi tmp değişkeni kullanın.
# İlk elemana tmp değerini verin.
# $\text{c) for döngüsü ve operatörünü kullanın.}$
# d) Yineleme için max() yöntemini ve uygun aralığı kullanın.
# e) pop() yöntemini ve // operatörünü kullanın.
# $\text{f) pop() ve insert() yöntemlerini ve operatörünü kullanın.}$
# $\text{h) Yineleme için uygun aralığı kullanın ve False if list[i] list[i+1] döndürün.}$
# i) Yineleme için uygun aralığı kullanın ve liste[i] == liste[i+1] ise True değerini döndürün.
# j) Listedeki her öğe için, tüm öğeler üzerinde tekrar yineleyin.
# Aynı değere sahip ancak farklı dizine sahip öğe varsa, True değerini döndürür.
# b) Son elemanın değerini tmp değişkenine kaydedin, diğer tüm elemanları kaydırın.
# %
# %
# g) Listeyi sıralayın, tüm öğeleri geriye doğru yineleyin
# ve son öğeden farklı olarak ilk geri dönün. 



