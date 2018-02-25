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

	def get_toilet(address):
		c = self.cursor()
		c.execute("select address from washrooms where address = " + address)

def open_database():
	#name = name + ".db"
	conn = sqlite3.connect("toiletbase.db")
	return conn

	#del m[2]
def locate_toilet(address):
	gmaps = googlemaps.Client(key="AIzaSyBx2FO-H9l_oQU8VL5xZI8msiBoYNO_1dM")
	geocode_result = gmaps.geocode(address)
	return (geocode_result[0]['formatted_address'],geocode_result[0]['geometry']['location'])

def get_toilet_from_database(address):


def main(): 
	conn = open_database()
	c = conn.cursor()
	c.execute("select X,Y from washrooms")
	(x,y) = c.fetchone()
	c.execute("select name, Address from washrooms")
	(name,address) = c.fetchone()
	#print(address)
	gmaps = googlemaps.Client(key="AIzaSyBx2FO-H9l_oQU8VL5xZI8msiBoYNO_1dM")

	formatted_address, location = locate_toilet(name + " " + address)
	
	c.execute("select address from washrooms where address = " + address)
	
	
	#print(geocode_result["address_components"]["lng"])
	#for row in c.execute("select * from washrooms"):
	#	print(c.fetchone())

if __name__ == "__main__":
    #app.run()
    main()