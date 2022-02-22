# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:15:26 2022

@author: Sümeyra Nihal GELMEZ
"""

# tic tac-toe oynayan bir program yazın.
#  Tic-tac-toe oyunu sağdaki fotoğrafta olduğu gibi 
#  3×3'lük bir ızgarada oynanmaktadır. Oyun sırayla 
#  iki oyuncu tarafından oynanır. İlk oyuncu hamleleri bir daire ile, 
#  ikincisi ise bir çarpı işaretiyle işaretler. Üç işaretten oluşan yatay, 
#  dikey veya çapraz bir dizi oluşturan oyuncu kazanır. 
#  Programınız oyun tahtasını çizmeli, kullanıcıdan bir sonraki 
#  işaretin koordinatlarını istemeli, her başarılı oyuncudan 
#  sonra oyuncuları değiştirmelidir.
# hareket et ve kazananı ilan et.
def ticTacToe():
 
 # initialize the table
 table = [ ["-"
, 
"-"
, 
"-"],
 ["-"
, 
"-"
, 
"-"],
 ["-"
, 
"-"
, 
"-"] ]
 
 # variable turn will tel us who takes turn 
 turn = 0
 printTable(table)
 
 while not isEnd(table):
 # if turn is even number 
 # first player takes a turn 
 if turn % 2 == 0:
 inputR = int(input("1. player enters a row (from 0 to 
 inputC = int(input("1. player enters a column (from 0 
 # check if inputs are valid 
while not isValid(inputR inputC table):


 print("Your inputs are not valid.")
 inputR = int(input("1. player enters a row (from 0 
 inputC = int(input("1. player enters a column (fro
 # and if inputs are valid, put "O" at given place 
 table[inputR][inputC] = "O"
 # turn is odd number
 # so second player takes a turn
 else: 
 inputR = int(input("2. player enters a row (from 0 to 
 inputC = int(input("2. player enters a column (from 0 
 while not isValid(inputR, inputC, table):
 print("Your inputs are not valid.")
 inputR = int(input("2. player enters a row (from 0 
 inputC = int(input("2. player enters a column (fro
 table[inputR][inputC] = "X"
 # increment turn
 turn = turn + 1
 # and print the current situation
 printTable(table)
 
# function checks if game is over
def isEnd(table):
 for i in range(3):
 # if there are 3 X or O in the row - game is over
 if table[i][0] == table[i][1] == table[i][2] == "X":
 print("Second player wins!")
 return True
 if table[i][0] == table[i][1] == table[i][2] == "O":
 print("First player wins!")
 return True
 # if there are 3 X or O in the column - game is over
 if table[0][i] == table[1][i] == table[2][i] == "X":
 print("Second player wins!")
 return True
 if table[0][1] == table[1][i] == table[2][i] == "O":
 print("First player wins!")
 return True
 
 # if there are 3 X or O on the main diagonal - game is over
 if table[0][0] == table[1][1] == table[2][2] == "X":
 print("Second player wins!")
 return True
 if table[0][0] == table[1][1] == table[2][2] == "O":
 print("First player wins!")
 return True
 
 # if there are 3 X or O on the secondary diagonal - game is ov
 if table[0][2] == table[1][1] == table[2][0] == "X":
 print("Second player wins!")
 return True
 if table[0][2] == table[1][1] == table[2][0] == "O":
 print("First player wins!")
 return True
 
 # if there are still empty elements in table
 # and function didn't return True 
 # this means that no one has won yet
 # and game is not over
 for i in range(3):
 for j in range(3):
 if table[i][j] == "-":
 return False
 
 # it means that function didn't return False 
 # in previous for loop 
 # in other words, there is no empty elements in the table
 # and no one has won
 # game is over
 print("No one has won!")
 return True
# function prints table
def printTable(table):
 for i in range(3):
 for j in range(2):
 print(str(table[i][j]) + " ", end = "")
 print(table[i][2])
 
# function checks if inputs are valid
def isValid(r, c, table):
 # if row or column is greater than 2
 # input in not valid
 if r > 2 or c > 2:
 return False
 # if row or column is smaller than 0
 # input is not valid
 if r < 0 or c < 0:
Egzersiz 27 Egzersiz 29
 if r < 0 or c < 0:
 return False
 # if the element on given position
 # is not empty
 # input is not valid
 if table[r][c] != "-":
 return False
 # else, input is valid
 return True
ticTacToe()