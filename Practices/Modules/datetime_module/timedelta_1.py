#!/usr/bin/env python3

import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)

print(tday - tdelta)


# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2020,1,26)
till_day = bday - tday
print(till_day.total_seconds())
