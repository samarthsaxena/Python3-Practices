#!/usr/bin/env python3

import datetime


t = datetime.time(9,30,20,23333)
print(t)
print(t.hour)

#this one gives access to everything
dt = datetime.datetime(2019,3,21,9,30,20,23333)
print(dt)
print(dt.date())
