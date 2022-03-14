# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:26:08 2022

@author: Sümeyra Nihal GELMEZ
"""

# a=[5,1,2,1,3,14]
# print(a)
# #list contains all integer 
# values=["red","blue","black","white"]
# print(values)   #the list containn all string
# b=["red",12,112.12]
# print(b)#the contains astring,an inreger,afloat numbers 

# b=[]
# print(b)
# #a list without any element is called an empthy list.
# color_list1=["white","yellow"]
# color_list2=["red","blue"]
# color_list3=["green","black"]
# color_list=color_list1+color_list2+color_list3
# print(color_list)

# number =[1,2,3]
# print(number[0]*4)
# print(number*4)
#use+ operator to create anew list that is aconcatenation of two lists and use * operatorto repeat a list


color_list=["red","blue","green","black"]
color_list[0] #return the first element
print(color_list[0],color_list[3])
color_list[-1]#return a last element
print(color_list[4])#creates error as the indices is out of range

color_list=["red","blue","green","black"]
print(color_list)

color_list.append("yellow")
print(color_list) #add an itemto the end of the list


#insert an item ata given position
color_list=["red","blue","green","black"]
print(color_list)

color_list.insert(2,white)
#insert an item at third position
print(color_list)
# ['Red', 'Blue', 'White', 'Green', 'Black']

color_list=["red","blue","green","black"]
print(color_list)

color_list[2]="yellow"
print(color_list)
# ['Red', 'Blue', 'Yellow', 'Black']
#remove an item from the list
color_list=["red","blue","green","black"]
print(color_list)
color_list.remove("black")
print(color_list)


#remove all items from the list
color_list=["Red", "Blue", "Green", "Black"]
print(color_list) 
color_list.clear()
print(color_list)
# <<<<[]
color_list=["Red", "Blue", "Green", "Black"]
print(color_list[0:2])
# ['Red', 'Blue']
#cut first two items
color_list=["Red", "Blue", "Green", "Black"]
print(color_list[1:2])
# ["blue"] 
print(color_list[1:-2])
# ["blue"]
color_list=["Red", "Blue", "Green", "Black"]
print(color_list[1:-1])
# ['Blue', 'Green'] 

#cut first three items from alist
color_list=["Red", "Blue", "Green", "Black"]
print(color_list[:3])
# ['Red', 'Blue', 'Green']


#creates copy of orginal list :
color_list=["Red", "Blue", "Green", "Black"]    
print(color_list[:])#cretates copt of original list
# ['Red', 'Blue', 'Green', 'Black']

color_list=["Red", "Blue", "Green"]
print(color_list)
color_list.pop(2)#remove second item an d return it
#"green
print(color_list)


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list.index("red")
#0
color_list.index("black")
#3

color_list=["Red", "Blue", "Green", "Black"]
print(color_list)           
#['Red', 'Blue', 'Green', 'Black']           
color_list=["Red", "Blue", "Green", "Black", "Blue"]
print(color_list)
#['Red', 'Blue', 'Green', 'Black', 'Blue']
color_list.count("blue")
#2


#sort the items of the list in olace
color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.sort(key=bone,reverse=False)
print(color_list)

#reverse the elements of the list in place
color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.reverse()
print(color_list)


#return a shallow copy of the list

color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.copy()


#search the lists and elements

color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.index("green")
#2
#lists are muutable
#items in the lists are mutable i.e after creating alist
#you can change any item in the list
color_list=["Red", "Blue", "Green", "Black"]
print(color_list[0])
#red
color_list[0]="white"
# "red
print(color_list)
color_list=["Red", "Blue", "Green", "Black"]
# >>> print(color_list[0])


#convert a list to a tuple in python


listx=[1,2,3,4]
print(listx)

tuplex=tuple(listx)
print(tuples)
# (1, 2, 3, 4)   


#how to use the double colon [::]?

listx=[1,5,7,3,2,4,6]
print(listx)

sublist=listx[2:7:2]
#list[start:stop:step]
#step specify incriment
print(sublist)
[7,2,6]

sublist=listx[::3]#returns a list with a jump every times2
print(sublist)
#[1,3,,6]


sublist=listx[6:2:-2]
#when step is negative the jump is made back
print(sublist)
[6,2]


#find the largest and th smallest item in alist
listx=[5,1,0,3,25,7,4,15]
print(listx)
print(max(listx))
#the ma x( function odf buit in allows to know the highest)

print(min(listx))
#the min() function of built in allows to know the lowest
#3
listx1, listx2=[3, 5, 7, 9], [3, 5, 7, 9]
print (listx1 == listx2)
True  
listx1, listx2=[9, 7, 5, 3], [3, 5, 7, 9]	#create two lists equal, but unsorted.
>>> print(listx1 == listx2)
False
>>> listx1, listx2 =[2, 3, 5, 7], [3, 5, 7, 9]	#create two different list
>>> print(listx1 == listx2)
False
>>> print(listx1.sort() == listx2.sort())	#order and compare
True

listx = [["Hello", "World"], [0, 1, 2, 3, 4, 5]]
>>> print(listx)
[['Hello', 'World'], [0, 1, 2, 3, 4, 5]]
>>> listx = [["Hello", "World"], [0, 1, 2, 3, 3, 5]]
>>> print(listx)
[['Hello', 'World'], [0, 1, 2, 3, 3, 5]]
>>> print(listx[0][1])		#The first [] indicates the index of the outer list.
World
>>> print(listx[1][3])		#the second [] indicates the index nested lists.
3
>>> listx.append([True, False])		#add new items
>>> print(listx)
[['Hello', 'World'], [0, 1, 2, 3, 3, 5], [True, False]]		
>>> listx[1][2]=4
>>> print(listx)
[['Hello', 'World'], [0, 1, 4, 3, 3, 5], [True, False]]		#update value items
>>>

>>> from collections import deque
>>> color_list = deque(["Red", "Blue", "Green", "Black"])
>>> color_list.append("White")      # White arrive
>>> print(color_list)
deque(['Red', 'Blue', 'Green', 'Black', 'White'])
>>> color_list.append("Yellow")     # Yellow arrive
>>> print(color_list)
deque(['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow'])
>>> color_list.popleft()            # The first to arrive now leaves
'Red'
>>> print(color_list)
deque(['Blue', 'Green', 'Black', 'White', 'Yellow'])
>>> color_list.popleft()            # The second to arrive now leaves
'Blue'
>>> print(color_list)
deque(['Green', 'Black', 'White', 'Yellow'])
>>> print(color_list)               # Remaining queue in order of arrival
deque(['Green', 'Black', 'White', 'Yellow'])
>>>











