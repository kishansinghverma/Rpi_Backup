import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    
    client.subscribe("bulb")
    client.subscribe("fan")
    client.subscribe("motor")


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())


client = mqtt.Client()
host = "klinux.tk"
port = 1883

client.connect(host, port, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
