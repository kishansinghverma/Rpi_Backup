from time import sleep
from gpiozero import InputDevice
from firebase import firebase
 
sensor = InputDevice(12)

firebase=firebase.FirebaseApplication('https://smarthomeautomation-1aa7c.firebaseio.com/',None)
x=1

while True:
    if not sensor.is_active :
        if(x==0):
            print("Tank Full!")
            firebase.put('','/water',1)
            x=1
    else:
        if(x==1):
            print("Water Level Dropped!")
            firebase.put('','/water',0)
            x=0
    sleep(1)
