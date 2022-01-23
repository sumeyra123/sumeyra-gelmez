# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:27:58 2022

@author: Sümeyra Nihal GELMEZ
"""

#Bir çalışanın adını ve maaşını okuyan bir program yazın. 
#Burada maaş, 9.25 dolar gibi saatlik bir ücret anlamına gelecektir. 
#Ardından, çalışanın geçen hafta kaç saat çalıştığını sorun. Kesirli saatleri kabul ettiğinizden emin olun. 
#Ödemeyi hesapla. Fazla mesai (haftada 40 saatten fazla) normal ücretin yüzde 150'si oranında ödenir.
#Çalışan için bir maaş çeki yazdırın.
# convert salary and hours to float-pointing numbers 
name = input("Enter a name of employee: ")
salary = float(input("Enter a salary (hourly wage): "))
hours = float(input("Enter a number of hours for past week: "))
# if hours are greater than 40 
# for first 40 hourly wage is normal
# for overtime work hourly wage is salary*1.5
if hours > 40:
 pay = 40 * salary
 payOvertime = (hours - 40) * salary * 1.5
 overtime = hours - 40
 regular = 40
# else, employee has less than 40 hours
# and total salary is hours*salary
else:
 pay = hours * salary
 payOvertime = 0
 overtime = 0
 regular = hours
 
# print paycheck
print("Employee " + str(name) + " worked " + str(hours)) 
print(str(name) + " has " + str(regular) + " regular hours and salary for its"+ str(pay))
print(str(name) + " has " + str(overtime) + " overtime hours and salary fotr its "+ str(payOvertime))
print("The total salary is " + str(payOvertime + pay))