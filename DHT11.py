import Adafruit_DHT
import datetime
import sqlite3
import time

conn = sqlite3.connect('log.db')

ptemp=0
phmd=0

while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    if((ptemp != temperature) or (phmd != humidity)):
        conn.execute('insert into temp values(null,'+str(temperature)+','+str(humidity)+',"'+datetime.datetime.now().strftime("%H:%M:%S")+'","'+datetime.datetime.now().strftime("%d-%m-%Y")+'");')
        ptemp=temperature
        phmd=humidity
    else:
        conn.execute("update temp set time='"+datetime.datetime.now().strftime("%H:%M:%S")+"' where id=(select id from temp order by id desc limit 1);")
    conn.commit()
    time.sleep(5)
