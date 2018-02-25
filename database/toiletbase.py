import sqlite3
import pandas
import numpy
import re
import googlemaps
from datetime import datetime
import json


class database:
	def __init__(self):
		self.db = open_database()

def open_database():
	#name = name + ".db"
	conn = sqlite3.connect("toiletbase.db")
	return conn

	#del m[2]


def main(): 
	conn = open_database()
	c = conn.cursor()
	c.execute("select X,Y from washrooms")
	(x,y) = c.fetchone()
	c.execute("select name, Address from washrooms")
	(name,address) = c.fetchone()
	#print(address)
	gmaps = googlemaps.Client(key="AIzaSyBx2FO-H9l_oQU8VL5xZI8msiBoYNO_1dM")

	#reverse_geocode_result = gmaps.reverse_geocode((y, x))
	geocode_result = gmaps.geocode(name + " " + address)
	print(geocode_result[0]['formatted_address'])
	print(geocode_result[0]['geometry']['location'])


	#print(geocode_result["address_components"]["lng"])
	#for row in c.execute("select * from washrooms"):
	#	print(c.fetchone())

if __name__ == "__main__":
    #app.run()
    main()