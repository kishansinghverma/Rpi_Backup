import time, sys
import RPi.GPIO as GPIO
import MQTT_Publisher
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x=0
def action(pin):
    global x
    x += 1
    if(x==2):
        print('Smoke Detected!!')
        MQTT_Publisher.publish("get/gas", "1")
        time.sleep(10)
        MQTT_Publisher.publish("get/gas", "0")
        x=0
        return
 
GPIO.add_event_detect(37, GPIO.RISING)
GPIO.add_event_callback(37, action)
 
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).
