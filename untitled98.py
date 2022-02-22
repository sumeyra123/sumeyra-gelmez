# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:55:10 2022

@author: Sümeyra Nihal GELMEZ
"""

# # Bir evcil hayvan dükkanı, bir veya daha fazla evcil hayvan ve en az beş başka ürün 
# satın alan müşterilerine indirim yapmak ister. İndirim, evcil hayvanların değil, diğer 
# öğelerin maliyetinin yüzde 20'sine eşittir. Bir işlev tanımlı 
# indirim uygulayın(fiyatlar, isPet, nItems)
# # İşlev, belirli bir satış hakkında bilgi alır. i. öğe için, fiyatlar[i] herhangi bir
#  indirimden önceki fiyattır ve öğe bir evcil hayvansa isPet[i] doğrudur. Kasiyerden 
#  her bir fiyatı girmesini ve ardından bir evcil hayvan için Y veya başka bir öğe için
#  N girmesini isteyen bir program yazın. Nöbetçi olarak –1 fiyatını kullanın. Girişleri bir 
#  listeye kaydedin. Uyguladığınız işlevi arayın ve indirimi görüntüleyin.
def discount(prices, isPet, nItems):
 # if there are no purchased pets
 # client doesn't have discount
 if not True in isPet:
   return 0
 # if there is less than 5 items
 # client doesn't have discount 
 if nItems < 5:
    return 0
 # otherwise, calculate sum of items
 # except pets
 sum = 0
 for i in range(len(prices)):
  if isPet[i] == False:
   sum = sum + prices[i]
 # and return 20% of this sum
 return sum * 0.2
prices = []
isPet = []
# number of items (without pets)
nItems = 0
userInput = float(input("Enter a price: "))
boolInput = input("Is it a pet (y/n): ")
while(userInput != -1):
 # if purchased item is pet 
 if boolInput.upper() == "Y":
 # add True to isPet list
  isPet.append(True)
 # add price to prices list 
 prices.append(userInput)
else: 
 # add False to isPet list 
 isPet.append(False)
 # increment number of items
 nItems = nItems + 1
 # and add price to prices list 
 prices.append(userInput)
userInput = float(input("Enter a price: "))
passboolInput = input("Is it a pet (y/n): ")
 
discount(prices, isPet, nItems)