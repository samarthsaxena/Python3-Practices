#!/usr/bin/python3

month_days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leapyear(year):

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_in_month(year, month):

	#Checking the validity of input month number
	if not 1 <= month <= 12:
		return f'Not a valid month. Please try in range 1 to 12.'

	#In case year is a leap year then Feb must be of 29 days
	if month == 2 and is_leapyear(year):
		return 29

	return month_days[month]



print(is_leapyear(2020))
print(is_leapyear(2017))
print(day_in_month(2020,2))
print(day_in_month(2017,2))
print(day_in_month(2018,5))
