import MQTT_Listener
import DHT
import Gas
import Water
import threading
import Assistant_Listener

p1 = threading.Thread(target=MQTT_Listener.startService) 
p2 = threading.Thread(target=DHT.startService)
p3 = threading.Thread(target=Gas.startService)
p4 = threading.Thread(target=Water.startService)
p5 = threading.Thread(target=Assistant_Listener.startService)

p1.start() 
p2.start()
p3.start()
p4.start()
p5.start()