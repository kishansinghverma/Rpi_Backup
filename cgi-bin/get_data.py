#!/usr/bin/python
import datetime
import sqlite3

conn = sqlite3.connect('log.db')
time=datetime.datetime.now().strftime("%H:%M:%S")
date=datetime.datetime.now().strftime("%d-%m-%Y")

fan=conn.execute('select * from fan order by id desc limit 1;')
bulb=conn.execute('select * from bulb order by id desc limit 1;')
dht=conn.execute('select * from temp order by id desc limit 1;')

fstat=0;
bstat=0;
temp=0;
humid=0;
time=str();
for x in fan:
    fstat=x[1]
    
for x in bulb:
    bstat=x[1]

for x in dht:
    temp=x[1]
    humid=x[2]
    time=x[3]


print('\n'+str(fstat)+'/'+str(bstat)+'/'+str(temp)+'/'+str(humid)+'/'+time)
    
    
