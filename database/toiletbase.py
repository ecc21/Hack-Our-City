import sqlite3
import pandas
import numpy
import re

def open_database():
	#name = name + ".db"
	conn = sqlite3.connect("toiletbase.db")
	return conn

	#del m[2]

def main(): 
	conn = open_database()
	c = conn.cursor()
	c.execute("select Name,Address from washrooms")
	data = c.fetchall()
	for row in data:
		print(row)

	#for row in c.execute("select * from washrooms"):
	#	print(c.fetchone())

if __name__ == "__main__":
    #app.run()
    main()