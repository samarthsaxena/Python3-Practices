#!/usr/bin/env python3

import datetime

d = datetime.date(2016,7,14)
print(d) #2016-07-14

tday= datetime.date.today()
print(tday)
print(tday.weekday())
print(tday.isoweekday())
print(tday.day)
