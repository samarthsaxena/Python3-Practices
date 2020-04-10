#!/usr/bin/env python3

import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days = 7)
bday = datetime.date(2019, 1, 26)

till_bday = bday - tday
print(till_bday.total_seconds()) 
