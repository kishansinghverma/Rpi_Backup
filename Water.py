from time import sleep
from gpiozero import InputDevice
import MQTT_Publisher
import Relay

def startService():
    print("Water Level Monitoring Started!")
    
    sensor = InputDevice(12)
    x=1
    while True:
        if not sensor.is_active :
            if(x==0):
                print("Tank Full!")
                Relay.switch("post/motor", "0")
                MQTT_Publisher.publish("get/water", "1")
                x=1
        else:
            if(x==1):
                print("Water Level Dropped!")
                MQTT_Publisher.publish("get/water", "0")
                x=0
        sleep(1)
