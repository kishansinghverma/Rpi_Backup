#!/usr/bin/python

import Adafruit_DHT
import datetime
import sqlite3

conn = sqlite3.connect('log.db')
dht=conn.execute('select * from temp order by id desc limit 1;')
    

for x in dht:
    temperature=x[1]
    humidity=x[2]
    time=x[3]
print("\n"+str(temperature)+"/"+str(humidity)+"/"+str(time))
