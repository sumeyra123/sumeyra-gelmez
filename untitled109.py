# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:38:18 2022

@author: Sümeyra Nihal GELMEZ
"""

# Binlerce uluslararası havalimanı hakkında bilgi içeren uzak bir veri dosyasından 
# elde edilen havalimanı adlarının bir listesini yazdıran bir program tasarlayın ve uygulayın.
# Dosya şurada bulunur
# https://sourceforge.net/p/openflights/code/HEAD/tree/openflights/data/airlines. 
import csv
import os

import wget
# function to get a list of all airport names
def get_list_all_airports(file_name):
 # empty list to store the list of
 # all airport names
 list_airports = []
 # get the current working directory
 cwd = os.getcwd()
 # store the full file path to the airport
 full_file_path = os.path.join(cwd, file_name)
 # file handler object
 file_handler = open(full_file_path)
 # iteratively get each row of the csv file
 # and store the airport name in the list
 for row in csv.reader(file_handler):
 airport_id = row[0]
 airport_name = row[1]
 # append the airport names in the list
 list_airports.append(airport_name)
 # return the list of all airports
 return list_airports
# function to display all the airports
def display_all_airports(list_airports):
 # Iteratively display all the airports in the list
 for i, airport in enumerate(list_airports):
 print(str(i+1), airport)
# driver method
def main():
 url = "https://sourceforge.net/p/openflights/code/HEAD/tree/op
 # download the airports from the url
 wget.download()
 file_name = "airlines.dat"
 # get a list of all airports
 list_airports = get_list_all_airports(file_name)
 # display all the airports
 display_all_airports(list_airports)
if __name__ == '__main__':
 main()