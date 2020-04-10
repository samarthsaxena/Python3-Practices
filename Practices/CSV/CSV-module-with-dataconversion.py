#!/usr/bin/env python3

import csv
from datetime import datetime


path = 'C:\\Users\\sasaxena\\AppData\\Local\\Programs\\Python\\Python37\\Practices\\CSV\\google_stock_data.csv'

#newLine arg with empty string ensures the end of the line does not have any \n char
file = open(path, newline='')

#reader() returns a reader object  <class '_csv.reader'>
reader = csv.reader(file)

#next() returns a List    <class 'list'>
#header will contain the first line of the csv, which is ['Date','Open','High','Low','Close','Volume','Adj Close']
header = next(reader)

data = list()

for row in reader:
    #row = [Date,Open,High,Low,Close,Volume,Adj Close]
    date = datetime.strptime(row[0],'%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date,open_price,high,low,close,volume,adj_close])

print(data[0])
for i in data[0]:
    print(type(i))
