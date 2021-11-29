import json
import sqlite3

# SQLite DB Name
DB_Name =  "IoT.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save water meter of KFC
def KFC_Water_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	nodeName = json_Dict['nodeName']
	Report_Time = json_Dict['reportTime']
	Value = json_Dict['meter']['meterReading'] #sub value of meter
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into KFC_Water_Data (nodeName, Report_Time, Value) values (?,?,?)",[nodeName, Report_Time, Value])
	del dbObj
	print("Inserted Temperature Data into Database.")
	print("")

# Function to save water meter of MandaiMart
def MandaiMart_Water_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	nodeName = json_Dict['nodeName']
	Report_Time = json_Dict['reportTime']
	Value = json_Dict['meter']['meterReading'] #sub value of meter
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into MandaiMart_Water_Data (nodeName, Report_Time, Value) values (?,?,?)",[nodeName, Report_Time, Value])
	del dbObj
	print("Inserted Temperature Data into Database.")
	print("")

# Function to save water meter of KFC
def BenNJerry_Water_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	nodeName = json_Dict['nodeName']
	Report_Time = json_Dict['reportTime']
	Value = json_Dict['meter']['meterReading'] #sub value of meter
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into BenNJerry_Water_Data (nodeName, Report_Time, Value) values (?,?,?)",[nodeName, Report_Time, Value])
	del dbObj
	print("Inserted Temperature Data into Database.")
	print("")

#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "organization/EEM/application/Non-Mage-Sensor/node/08000000700000b8/rx":
		KFC_Water_Data_Handler(jsonData)
	elif Topic == "organization/EEM/application/Non-Mage-Sensor/node/08000000700000b9/rx":
		MandaiMart_Water_Data_Handler(jsonData) 		
	elif Topic == "organization/EEM/application/Non-Mage-Sensor/node/08000000700000ba/rx":
    		BenNJerry_Water_Data_Handler(jsonData)

#===============================================================
