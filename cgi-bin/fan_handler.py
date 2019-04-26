#!/usr/bin/python

import cgi, cgitb
import datetime
import sqlite3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



form = cgi.FieldStorage() 
fan= form.getvalue('fan')

if(fan!=None):
    print('\n'+fan)
    conn = sqlite3.connect('log.db')
    time=datetime.datetime.now().strftime("%H:%M:%S")
    date=datetime.datetime.now().strftime("%d-%m-%Y")
    user='user';
    conn.execute('insert into fan values(null,"'+fan+'","'+user+'","'+time+'","'+date+'");')
    conn.commit()
    GPIO.setup(23, GPIO.OUT)
    if(fan=='1'):
        GPIO.output(23, False)
    else:
        GPIO.output(23, True)
else:
    print('\nError')





