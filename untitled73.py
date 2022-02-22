# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:52:49 2022

@author: Sümeyra Nihal GELMEZ
"""

# Bu ödevde, Bulgar Solitaire oyununu modelleyeceksiniz. Oyun 45 kartla başlar. 
# (Oyun kartları olmalarına gerek yoktur. İşaretlenmemiş dizin kartları da aynı şekilde çalışır.) 
# Bunları rastgele büyüklükte birkaç yığına rastgele bölün. Örneğin, 20, 5, 1, 9 ve 10 büyüklüğünde yığınlarla başlayabilirsiniz. 
# Her turda, her yığından bir kart alarak bu kartlarla yeni bir yığın oluşturursunuz. Örneğin, numune başlangıç 
# konfigürasyonu 19, 4, 8, 9 ve 5 büyüklüğünde yığınlara dönüştürülecektir. Yığınlar 1, 2, 3, 4, 5, 6, 7, 8, ve 9, bir sırayla. 
# (Her zaman böyle bir konfigürasyonla karşılaştığınız gösterilebilir.) Programınızda rastgele bir başlangıç konfigürasyonu oluşturun ve yazdırın. 
# Ardından soli taire adımını uygulamaya devam edin ve sonucu yazdırın. solitaire nihai konfigürasyonuna ulaşıldığında durun. 
import random 
# input is number of piles at the beginning
def bulgarianSolitaire(num):
 piles = []
 cards = 45
 # first configuration
 for i in range(num-1):
 x = random.randint(1, cards)
 # number of cards in pile can't be 0
 # so first pile must have numbers of cards 
 # between 1 and 45 - num + 1 (inclusive)
 # for example for num = 5
 # first pile can have between 1 and 41 cards
 # because if first pile has 42 cards
 # one of remaining 4 must have 0 cards
 while x > cards - num + i + 1: 
 x = random.randint(1, cards)
piles append(x)

 piles.append(x)
 cards = cards - x
 piles.append(cards)
 # print first configuration
 print(piles)
 
 # check if game is over
 while not isOver(piles):
 # and if it not, make next configuration 
 # and print it 
 nextStep(piles)
 print(piles)
 
 
# function makes next configuration of piles 
def nextStep(piles):
 # last element in new configuration is number of piles 
 # in current configuration 
 last = len(piles)
 pos = 0
 # iterate over all piles and take one card from each
 while pos < len(piles):
 # if there is only 1 card left
 # there is no more that pile
 # so remove it 
 if piles[pos] == 1:
 piles.pop(pos)
 # if there is more than 1 card, take one
 else:
 piles[pos] = piles[pos] - 1
 pos = pos + 1
 # add new pile 
 piles.append(last)
 
# function checks if game is over 
def isOver(piles):
 # for i between 1 and 9 (inclusive)
 for i in range(1, 10):
 # if i is not in the list game is not over
 if i not in piles:
 return False
 # if loop is completed without returning False
 # we have piles of sizes 1, 2, 3, 4, 5, 6, 7, 8 and 9
 # in some order

 # and game is over
 return True
bulgarianSolitire(5)
