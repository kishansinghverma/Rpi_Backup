import paho.mqtt.client as mqtt

def publish(topic, msg):
    client = mqtt.Client()
    host = "klinux.tk"
    port = 1883
    client.connect(host, port, 60)
    client.publish(topic,msg,retain=True)
    client.disconnect()
    