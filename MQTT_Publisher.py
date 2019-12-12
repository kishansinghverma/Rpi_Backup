import paho.mqtt.client as mqtt
import Firebase_Publisher
import Connection

def publish(topic, msg):
    print("Publishing to the given topic!")
    
    host=Connection.host
    port=Connection.port
    
    client = mqtt.Client()
    client.connect(host, port, 60)
    client.publish(topic,msg,retain=True)
    client.disconnect()
    
    Firebase_Publisher.setTime()
    