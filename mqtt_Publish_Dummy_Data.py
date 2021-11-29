#use this script only for testing
#if live data source is present, this should not be used
import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

#====================================================
# MQTT Settings 
MQTT_Broker = "asia.srv.sindconiot.com"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_KFC = "organization/EEM/application/Non-Mage-Sensor/node/08000000700000b8/rx" #
MQTT_Topic_MandaiMart = "organization/EEM/application/Non-Mage-Sensor/node/08000000700000b9/rx"
MQTT_Topic_BenNJerry = "organization/EEM/application/Non-Mage-Sensor/node/08000000700000ba/rx"
#====================================================

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		

		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print("")


#====================================================
# FAKE SENSOR 
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

toggle = 0

def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		KFC_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))

		KFC_Data = {}
		KFC_Data['nodeName'] = ""
		KFC_Data['Report_Time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		KFC_Data["meter"] = KFC_Fake_Value
		KFC_json_data = json.dumps(KFC_Data)

		print("Publishing fake KFC Value: " + str(KFC_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_KFC, KFC_json_data)
		toggle = 1

	elif toggle == 1:
		MandaiMart_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))

		MandaiMart_Data = {}
		MandaiMart_Data['nodeName'] = "Dummy-2"
		MandaiMart_Data['Report_Time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		#MandaiMart_Data['meter']['meterReading'] = MandaiMart_Fake_Value
		MandaiMart_json_data = json.dumps(MandaiMart_Data)

		print("Publishing fake MandaiMart Value: " + str(MandaiMart_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_MandaiMart, MandaiMart_json_data)
		toggle = 2
	
	elif toggle == 2:
		BenNJerry_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))

		BenNJerry_Data = {}
		BenNJerry_Data['nodeName'] = "Dummy-2"
		BenNJerry_Data['ReportTime'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		#BenNJerry_Data['meter']['meterReading'] = BenNJerry_Fake_Value
		BenNJerry_json_data = json.dumps(BenNJerry_Data)

		print("Publishing fake BenNJerry Value: " + str(BenNJerry_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_BenNJerry, BenNJerry_json_data)
		toggle = 0
	
publish_Fake_Sensor_Values_to_MQTT()

#====================================================
