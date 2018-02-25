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

	def get_toilet(self, address):
		c = self.db.cursor()
		#should probably add a date_added column...
		c.execute("select address from washrooms where address = \"" + address + "\";")
		a = c.fetchone()
		if a != None:
			return(a[0])
		else:
			return ""

	def add_toilet(self, address, name = None,lat = None, lng = None ):
		if name == None:
			name = "NULL"
		else:
			name = "\"" + name + "\""
		if lat == None:
			lat = "NULL"
		if lng == None:
			lng = "NULL"
		c = self.db.cursor()
		#if self.get_toilet(address) == "":
		print("adding toilet to washrooms")
		address = "\"" + address + "\""
		c.execute("insert into washrooms values(%s, %s, %s, %s);" % (address,name,str(lat),str(lng)))
		self.db.commit()
		#else:
		#	address = "\"" + address + "\""
		#	c.execute("update washrooms set name = %s, lat = %s, lng = %s where address = %s;" % (name,str(lat),str(lng),address))
		#	#c.execute("insert into washrooms values(%s, %s, %s, %s)" % (address,"?","?","?"))
		#	self.db.commit()


def open_database():
	#name = name + ".db"
	conn = sqlite3.connect("test.db")
	return conn

	#del m[2]
def locate_toilet(address):
	gmaps = googlemaps.Client(key="AIzaSyBx2FO-H9l_oQU8VL5xZI8msiBoYNO_1dM")
	geocode_result = gmaps.geocode(address)
	return (geocode_result[0]['formatted_address'],geocode_result[0]['geometry']['location'])


def main(): 
	conn = open_database()
	c = conn.cursor()
	db = database()
	#c.execute("select lng,lat from washrooms")
	#(x,y) = c.fetchone()
	#c.execute("select name, Address from washrooms")
	#(name,address) = c.fetchone()
	#print(address)
	gmaps = googlemaps.Client(key="AIzaSyBx2FO-H9l_oQU8VL5xZI8msiBoYNO_1dM")
	reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
	formatted_address = reverse_geocode_result[0]['formatted_address']
	db.add_toilet(formatted_address)
	c.execute("select address from washrooms where address = \"" + formatted_address + "\";")
	#print(c.fetchone())
	#print(db.get_toilet(formatted_address))

	#formatted_address, location = locate_toilet(name + " " + address)
	
	#c.execute("select address from washrooms where address = \"" + address + "\"")

	#c.execute("insert into washrooms values(%s, %s, %f, %f)" % (address,name,lat,lng))
	
	
	#print(geocode_result["address_components"]["lng"])
	#for row in c.execute("select * from washrooms"):
	#	print(c.fetchone())

if __name__ == "__main__":
    #app.run()
    main()