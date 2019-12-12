import paho.mqtt.client as mqtt
import time
import Relay
import Connection

def on_connect(client, userdata, flags, rc):
    print("Connected To MQTT Server")
    
    client.subscribe("post/bulb")
    client.subscribe("post/fan")
    client.subscribe("post/motor")


def on_message(client, userdata, msg):
    Relay.switch(msg.topic, msg.payload.decode())
    

def startService():
    print(">> MQTT Listener Service Started")
    
    host=Connection.host
    port=Connection.port
    
    client = mqtt.Client()
    client.connect(host, port, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

