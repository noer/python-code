from gpiozero import LED
from gpiozero import Button
from time import sleep

lg = LED(18)
ly = LED(19)
lr = LED(20)
btn = Button(24)
status = "G"
lg.on()

def red_to_green():
    global status
    print("red_to_green")
    status = "G"
    ly.on()
    sleep(1)
    lr.off()
    ly.off()
    lg.on()

def green_to_red():
    global status
    print("green_to_red")
    status = "R"
    lg.off()
    ly.on()
    sleep(1)
    ly.off()
    lr.on()

def switch_lights():
    if(status == "G"):
        green_to_red()
    elif(status == "R"):
        red_to_green()

btn.when_activated = switch_lights


sleep(1000)

"""
while True:
    red_to_green()
    sleep(10)
    green_to_red()
    sleep(10)
"""
