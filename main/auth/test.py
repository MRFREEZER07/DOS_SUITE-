import authclass 
import datetime
import dateutil.relativedelta
import time
import subprocess
import os
a=authclass.Auth()
d1=1665860322.562075
d2=time.time()
def timeDifference(d1,d2):

    dt1 = datetime.datetime.fromtimestamp(d1) # 1973-11-29 22:33:09
    dt2 = datetime.datetime.fromtimestamp(d2) # 1977-06-07 23:44:50
    rd = dateutil.relativedelta.relativedelta (dt2, dt1)
    print(rd)
    print(rd.years)
    return "%d years, %d months, %d days, %d hours, %d minutes and %d seconds" % (rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds)


def epochTimeToNormal(time):
    value = datetime.datetime.fromtimestamp(time)
    print( value.strftime('%Y-%m-%d %H:%M:%S'))

z =timeDifference(d1,d2)
print(z)