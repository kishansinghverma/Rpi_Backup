#!/usr/bin/python

import cgi, cgitb
import datetime
import sqlite3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

form = cgi.FieldStorage() 
bulb= form.getvalue('bulb')

if(bulb!=None):
    print('\n'+bulb)
    conn = sqlite3.connect('log.db')
    time=datetime.datetime.now().strftime("%H:%M:%S")
    date=datetime.datetime.now().strftime("%d-%m-%Y")
    user='user';
    conn.execute('insert into bulb values(null,"'+bulb+'","'+user+'","'+time+'","'+date+'");')
    conn.commit()
    GPIO.setup(22, GPIO.OUT)
    if(bulb=='1'):
        GPIO.output(22, False)
    else:
        GPIO.output(22, True)
else:
    print('\nError')





