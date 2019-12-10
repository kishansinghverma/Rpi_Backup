  
import RPi.GPIO as GPIO
from time import sleep
import time
import MQTT_Publisher

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [1, 7, 8, 25]
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)
GPIO.setup(pins[3], GPIO.OUT)

OFF=GPIO.HIGH
ON=GPIO.LOW

GPIO.output(pins[0], OFF)
GPIO.output(pins[1], OFF)
GPIO.output(pins[2], OFF)
GPIO.output(pins[3], OFF)

    
def switch(topic, msg):
    print("Relay service initiated!")
    
    if(topic=="post/bulb"):
        if(msg=="1"):
            GPIO.output(pins[0], ON)
        else:
            GPIO.output(pins[0], OFF)
    
        MQTT_Publisher.publish("get/bulb", msg)
        
    elif(topic=="post/fan"):
        if(msg=="1"):
            GPIO.output(pins[1], ON)
        else:
            GPIO.output(pins[1], OFF)
    
        MQTT_Publisher.publish("get/fan", msg)
        
    elif(topic=="post/motor"):
        if(msg=="1"):
            GPIO.output(pins[2], ON)
        else:
            GPIO.output(pins[2], OFF)
    
        MQTT_Publisher.publish("get/motor", msg)
        
        