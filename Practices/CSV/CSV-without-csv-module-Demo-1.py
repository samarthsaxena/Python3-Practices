#!/usr/bin/env python3

def looping_through_list(list_of_items):
    for i in list_of_items:
        print(i)
        print('-' * len(i))
    return


file_path = 'C:\\Users\\sasaxena\\AppData\\Local\\Programs\\Python\\Python37\\Practices\\CSV\\google_stock_data.csv'

entries = []

with open(file_path,'r') as f:
    for entry in f:
        entries.append(entry.strip().split(','))

print(len(entries))
looping_through_list(entries)

#But the data in the csv is always in String, so we need a better approach to convert this data into respective datatype too.
