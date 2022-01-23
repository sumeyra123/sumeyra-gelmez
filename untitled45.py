# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:40:50 2022

@author: Sümeyra Nihal GELMEZ
"""

#Bir süpermarket, bir müşterinin bakkaliye ne kadar harcadığına bağlı olarak kuponlar verir. Örneğin, 50 dolar harcarsanız, bu tutarın yüzde sekizi değerinde bir kupon alırsınız. Aşağıdaki tabloda, harcanan farklı tutarlar için verilen kuponu hesaplamak için kullanılan yüzde gösterilmektedir. Bir kişinin satın aldığı ürünleri temel alarak alabileceği kuponun değerini hesaplayan ve basan bir program yazın. İşte örnek bir çalışma:
#Lütfen ürünlerinizin maliyetini girin: 14
#1.12 $ indirim kuponu kazanırsınız. (satın alma işleminizin% 8'i)
# convert input to float-pointing number 
cost = float(input("Please enter the cost of your groceries: "))
# If customer spends less than $10, 
# he will not get a coupon
if cost < 10:
 print("No coupon.")
# for spent money between$10 and $60
# coupon is 8%
elif 10 <= cost < 60:
 coupon = 8
 discount = cost * 0.08
# and so on 
elif 60 <= cost < 150:
 coupon = 10
 discount = cost * 0.1
elif 150 <= cost < 210:
 coupon = 12
 discount = cost * 0.12
# in this case
# customers spends more than$210 
else:
 coupon = 14
 disconut = cost * 0.14
 
print("You win a discount coupon of $" + str(discount) + " (" + str (coupon) + " (% of your purchase)")
