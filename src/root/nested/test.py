'''
Created on Oct 19, 2013

@author: Yuan-Fang
'''
from datetime import datetime, timedelta
import time

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time :", localtime

yr_ago=ticks-timedelta(days=365).seconds

print yr_ago