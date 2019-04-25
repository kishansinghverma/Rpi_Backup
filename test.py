import sqlite3
import datetime

conn = sqlite3.connect('log.db')
print ("Opened database successfully");

print(datetime.datetime.now().strftime("%d-%m-%Y"))
