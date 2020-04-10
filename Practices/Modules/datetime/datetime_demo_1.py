#!/usr/bin/env python3

import datetime

#Available modules and methods
print(dir(datetime))
print(datetime.MAXYEAR, "  ", datetime.MINYEAR," ", datetime.tzinfo())

#This is to formate the date in according to your need
date = datetime.date(1994, 1, 26)
print(date)


#Current day
today = datetime.date.today()
print('Today\'s date is : ',today)
print("Today's year : ",today.year)
print("Today's month : ",today.month)
print("Today's day : ",today.day)

#How to print weekday
# weekday()         Mondya = 0 and Sunday = 6
# isoweekday()      Monday = 1 and Sunday = 7
print(today.weekday())
print(today.isoweekday())


#timedelta
#timedelta  defines number of days that needs to added/subtracted/calculated with dates
#basically it's a tool to perform  arithmetics on dates
tdelta = datetime.timedelta(days = 10)

date_with_timedelta_add = today +  tdelta # adds 10 days period too today's date
date_with_timedelta_sub = today - tdelta # subtracts 10 days period from today's date
print('date_with_timedelta_add : ',date_with_timedelta_add)
print('date_with_timedelta_sub : ',date_with_timedelta_sub)

#date1 = date2 +   -   timedelta
#timedelta = date1 -   = date2
