#!/usr/bin/python

import cgi, cgitb
import datetime
import sqlite3

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
else:
    print('\nError')





