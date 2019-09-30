import paho.mqtt.client as client

mqtt = client.Client()
mqtt.connect('localhost')

mqtt.publish('testTopic', "python test")
