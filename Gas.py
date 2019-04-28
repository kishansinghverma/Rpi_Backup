import time, sys
import RPi.GPIO as GPIO
from firebase import firebase
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

firebase=firebase.FirebaseApplication('https://smarthomeautomation-1aa7c.firebaseio.com/',None)

x=0
def action(pin):
    global x
    x += 1
    if(x==2):
        print('Smoke Detected!!')
        firebase.put('','/smoke',1)
        time.sleep(10)
        firebase.put('','/smoke',0)
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
