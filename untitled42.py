# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:21:09 2022

@author: Sümeyra Nihal GELMEZ
"""

#Bir banka işlemini simüle etmek için bir program yazın. İki banka hesabı vardır: çek ve tasarruf. 
#İlk olarak, banka hesaplarının başlangıç bakiyelerini isteyin; negatif bakiyeleri reddedin.
#Ardından işlemi isteyin; seçenekler para yatırma, çekme ve aktarmadır. 
#Ardından hesabı isteyin; seçenekler kontrol ve tasarruftur. Ardından tutarı isteyin; bir hesabı fazla çeken işlemleri reddedin.#
# Sonunda bakiyeleri yazdırın
#hem hesapları.

balanceChecking = float(input("Enter your balance of checking account":))
# reject negative balances
if balanceChecking < 0:
 raise Exception("Balances can't be negative.")
balanceSaving = float(input("Enter your balance of saving account:))
if balanceSaving < 0:
 raise Exception("Balances can't be negative.")
transaction = input("Transaction? Options are deposit (d), withdraw
account = input("Checking(c) or savings(s) account: ")
amount = float(input("Amount: "))
if account.upper() == "C":
 # if transaction is deposit
 # it doesn't matter how much money
 # user has at account
 # since we add entered amount of money 
 # on the account
if transaction upper() == "D":

 if transaction.upper() == D :
 balanceChecking += amount
 # chosen transaction is withdrawal or transfer
 # in any case, we need to subtract some money
 # from the account, so you need to check 
 # if user has enough money 
 else:
 # if doesn't, print error message
 if balanceChecking < amount:
 print("You don't have enough money at checking account
 # else, if transaction is withdrawal 
 # just subtract entered amount of money 
 else:
 if transaction.upper() == "W":
 balanceChecking -= amount
 # otherwise, if transaction is transfer
 # subtract from the checking account
 # and add to saving account
 else:
 balanceChecking -= amount
 balanceSaving += amount 
 
# same logic with the saving account
else:
 if transaction.upper() == "D":
 balanceSaving += amount
 else:
 if balanceSaving < amount:
 print("You don't have enough money at saving account."
 else:
 if transaction.upper() == "W":
 balanceSaving -= amount
 else:
 balanceSaving -= amount
 balanceChecking += amount 
 
# at the end, print current balances 
print("Checking: " + str(balanceChecking))
print("Saving: " + str(balanceSaving))
