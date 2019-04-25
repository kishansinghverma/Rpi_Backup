#!/usr/bin/python

import Adafruit_DHT
import datetime
import sqlite3

conn = sqlite3.connect('log.db')
time=datetime.datetime.now().strftime("%H:%M:%S")
date=datetime.datetime.now().strftime("%d-%m-%Y")
    
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print("\n"+str(temperature)+"/"+str(humidity)+"/"+str(time))
conn.execute('insert into temp values(null,'+str(temperature)+','+str(humidity)+',"'+time+'","'+date+'");')
conn.commit()
