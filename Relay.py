import RPi.GPIO as GPIO  # Import GPIO Module
from time import sleep
import time# Import sleep Module for timing

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings

pins = [22, 23, 24, 25]  # Set the GPIO pins that are required

#Set our GPIO pins to outputs and set them to off

while(True):
    for i in range(len(pins)):
        
        
        GPIO.setup(pins[i%4], GPIO.OUT)
        GPIO.output(pins[i%4], False)
        time.sleep(0.05)

        GPIO.setup(pins[(i+1)%4], GPIO.OUT)
        GPIO.output(pins[(i+1)%4], False)
        time.sleep(0.05)

        GPIO.setup(pins[i%4], GPIO.OUT)
        GPIO.output(pins[i%4], True)
        time.sleep(0.05)

        GPIO.setup(pins[(i+1)%4], GPIO.OUT)
        GPIO.output(pins[(i+1)%4], True)
        time.sleep(0.05)
        
    
