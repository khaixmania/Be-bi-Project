#Code pour le babyphone des parents
from microbit import *
import radio

radio.config(group=22)
radio.on()

while True : 
    if button_a.was_pressed() :
        radio.send("hello")

    message2 = radio.receive()
    if message2 : 
        display.scroll(message2)

