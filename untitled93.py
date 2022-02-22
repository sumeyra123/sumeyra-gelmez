# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 15:24:17 2022

@author: Sümeyra Nihal GELMEZ
"""

fo= open("jale.txt","w")
(fo.write("merhaba Türk milleti"))
fo.close()
dosya=open("jale.txt","a")
dosya.write("\nnihal")
dosya.close()

# a	Eklemek için bir dosya açar. Dosya varsa dosya işaretçisi dosyanın sonundadır. Dosya mevcut değilse, yazmak için yeni bir dosya oluşturur
# w	Sadece yazmak için bir dosya açar. Dosya varsa, dosyanın üzerine yazar. Dosya yoksa, yazmak için 
# r	Sadece okumak için bir dosya açar. Dosya işaretçisi, dosyanın başına yerleştirilir. Bu varsayılan moddur.
# r+	Hem okuma hem de yazma için bir dosya açar.
