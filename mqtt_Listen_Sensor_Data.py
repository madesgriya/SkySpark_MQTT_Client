import paho.mqtt.client as mqtt
import json
from store_Sensor_Data_to_DB import sensor_Data_Handler

# MQTT Settings 
MQTT_Broker = "asia.srv.sindconiot.com"
user = "_APP_teale"
password = "fVWhGmcLfZl1"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "organization/EEM/application/Non-Mage-Sensor/node/#" 

#Subscribe to all Sensors at Base Topic
#def on_connect(mosq, obj, rc):
def on_connect(mosq, obj, rc, rx):
	mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print("MQTT Data Received...")
	print("MQTT Topic: " + msg.topic)
	#print("Data: " + msg.payload)  
	global json_str
	json_str = json.loads(msg.payload.decode())
	print("Data: " + str(json_str))
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.username_pw_set(user, password=password) 

# Continue the network loop
mqttc.loop_forever()
