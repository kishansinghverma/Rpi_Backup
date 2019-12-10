from Adafruit_IO import MQTTClient
import Relay

def connected(client):
    print('Connected to Adafruit IO!')
    client.subscribe('bulb')
    client.subscribe('fan')
    client.subscribe('motor')
    

def message(client, feed_id, payload):
    Relay.switch("post/"+feed_id, payload)

def startService():
    print(">> Assitant Listner service started!")
    ADAFRUIT_IO_KEY = '8c61ee1ac0f0421f96512e30be6b30dc'
    ADAFRUIT_IO_USERNAME = 'Kishansinghverma1'
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    client.on_connect    = connected
    client.on_message    = message
    client.connect()
    client.loop_blocking()

