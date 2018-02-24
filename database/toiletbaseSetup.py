import sqlite3
import pandas
import numpy
import re

def create_database(name):
	#name = name + ".db"
	conn = sqlite3.connect(name)
	return conn

def open_csv(name):
	df = pandas.read_csv(name)
	return df

def clean_dataframe(dataframe):
	df = dataframe[['Name', 'Category', 'Address','X','Y',
					'Monday','Tuesday','Wednesday',
					'Thursday', 'Friday', 'Saturday',
					'Sunday', 'Accessible']]
	return df

#def to_twenty_four_clock(time_string):
	##m = re.split('[ ,:]', time_string)
	#if m[6] == "pm":
	#	hour = int(m[4]) + 12
	#	m[4] = hour
	#if m[2] == "pm": 
	#	hour = int(m[2]) + 12
	#	m[2] = hour
	#del m[6]
	#del m[2]

def main(): 
	conn = create_database("toiletbase.db")
	csv = open_csv("WASHROOMS.CSV")
	#print(csv)
	dataframe = clean_dataframe(csv)
	#print(dataframe)
	#print(csv["Monday"][1])

	#print(m)
	dataframe.to_sql("washrooms", conn)
	#c = conn.cursor()
	#c.execute("select * from washrooms")
	#data = c.fetchall()
	#print(data[1])

	#for row in c.execute("select * from washrooms"):
	#	print(c.fetchone())

if __name__ == "__main__":
    #app.run()
    main()