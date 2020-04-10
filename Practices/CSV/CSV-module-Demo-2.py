#!/usr/bin/env python3
import csv

path = 'C:\\Users\\sasaxena\\AppData\\Local\\Programs\\Python\\Python37\\Practices\\CSV\\google_stock_data.csv'

file = open(path, newline='')

reader = csv.reader(file)

header = next(reader)

# [row for row in reader]  by this every data would be treated as string.
data =[]
for row in reader:
