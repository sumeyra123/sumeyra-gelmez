# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:37:44 2022

@author: Sümeyra Nihal GELMEZ
"""

#Banka kartınızla birlikte otomatik vezne makinesi (ATM) kullandığınızda, hesabınıza erişmek için kişisel kimlik numarası (PIN) kullanmanız gerekir. Bir kullanıcı PIN'i girerken üç defadan fazla başarısız olursa, makine kartı bloke eder. 
#Kullanıcının pın'inin “1234” olduğunu varsayalım ve kullanıcıdan PIN'i en fazla üç kez isteyen ve aşağıdakileri yapan bir program yazın: • Kullanıcı doğru numarayı girerse, “Pın'iniz doğru” yazan bir mesaj yazdırın ve programı sonlandırın.
#• Kullanıcı yanlış bir numara girerse, “Pın'iniz yanlış” yazan bir mesaj yazdırın ve PIN'i üç defadan az sorduysanız, tekrar sorun.
#• Kullanıcı üç kez yanlış numara girerse, “Sizin numaranız" yazan bir mesaj yazdırın.
#banka kartı bloke edildi" ve programı sonlandırın.
pin = input("Enter a PIN: ")
# first mistake
if pin != "1234":
 print("Your PIN is incorrect.")
 pin = input("Enter a PIN: ")
 # second mistake
 if pin != "1234":
 print("Your PIN is incorrect.")
 pin = input("Enter a PIN: ")
 # third mistake
 if pin != "1234":
 print("Your bank card is blocked.")
 else:
 print("Your PIN is correct.")
 else:
 print("Your PIN is correct.")
else:
 print("Your PIN is correct.")
