import paho.mqtt.client as client
from gpiozero import Button
import json

btn_red = Button(21)
btn_blue = Button(20)
btn_yellow = Button(19)
btn_green = Button(18)

mqtt = client.Client()
mqtt.connect('localhost')

mqtt.publish('easv/iot.rasp.19/rating', json.dumps({"status": "connected"}))


def btn_rating(rating):
    mqtt.publish('easv/iot.rasp.19/rating', json.dumps({"rating": rating}))

def b_red():
    print("red1")
    btn_rating(1)

def b_blue():
    print("red2")
    btn_rating(2)

def b_yellow():
    print("red3")
    btn_rating(3)

def b_green():
    print("red4")
    btn_rating(4)


btn_red.when_activated = b_red
btn_blue.when_activated = b_blue
btn_yellow.when_activated = b_yellow
btn_green.when_activated = b_green

mqtt.loop_forever()


