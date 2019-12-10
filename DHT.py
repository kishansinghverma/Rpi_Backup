import Adafruit_DHT
import time
import MQTT_Publisher
import Firebase_Publisher
    

def startService():
    print(">> Temperature Monitoring Service Started!")
    
    h=0; t=0
    
    while True:
        humidity, temp = Adafruit_DHT.read_retry(11, 14)
        
        if(h != humidity or t!=temp):
            h=humidity
            t=temp
            MQTT_Publisher.publish("get/dht", str(t)+"/"+str(h))
            Firebase_Publisher.publish(t, h)
            
        time.sleep(1)
