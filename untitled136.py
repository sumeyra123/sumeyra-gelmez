# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:23:46 2022

@author: Sümeyra Nihal GELMEZ
"""
def main():
 a=int(input("please enter your number:"))
 print (mukemmel(a)) 
def mukemmel(sayı):
        
    toplam = 0

    for i in range(1,sayı):
        
        if (sayı % i == 0):
            toplam += i
        return toplam==sayı  
        for i in (sayı):
             print("Mükemmel Sayı:",i)
      
main()             