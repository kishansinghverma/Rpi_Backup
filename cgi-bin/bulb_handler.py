#!/usr/bin/python

import cgi, cgitb
import datetime
import sqlite3

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
else:
    print('\nError')





