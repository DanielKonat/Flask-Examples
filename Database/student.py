import sqlite3

conn=sqlite3.connect('database.db')
print("Opened database sucessfully")

conn.execute('create table abc(name TEXT,addr TEXT,city TEXT,pin TEXT)')
print("table created sucessfully")

conn.close()
