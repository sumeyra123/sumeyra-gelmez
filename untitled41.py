# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:18:10 2022

@author: Sümeyra Nihal GELMEZ
"""
#The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a given month and day.
#If month is 1, 2, or 3, season = "Winter" Else if month is 4, 5, or 6, season = "Spring" Else if month is 7, 8, or 9, season = "Summer" Else if month is 10, 11, or 12, season = "Fall" If month is divisible by 3 and day >= 21 If season is "Winter", season = "Spring" Else if season is "Spring", season = "Summer" Else if season is "Summer", season = "Fall" Else season = "Winter"
#Write a program that prompts the user for a month and day and then prints the season, as determined
#by this algorithm.
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
# just shorter syntax for: 
# if month == 1 or month == 2 or month == 3
if month in {1, 2, 3}:
 season = "Winter"
elif month in {4, 5, 6}:
 season = "Spring"
elif month in {7, 8, 9}:
 season = "Summer"
elif month in {10, 11, 12}:
 season = "Fall"
 
# if month is divisible by 3
# and day is greater or equal to 21
if month % 3 == 0 and day >= 21:
 # update the season
 if season == "Winter":
   season = "Spring"
 elif season == "Spring":
  season = "Summer"
 elif season == "Summer":
  season = "Fall"
 else:
  season = "Winter"
 
print(season)
