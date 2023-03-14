from microbit import *
import radio
import log

radio.config(group=4)
radio.on()
log.delete(True)

while True:
    def update():
        mic=microphone.sound_level()
        magne=compass.heading()
        light1=display.read_light_level()
        
        if mic > 75:
            radio.send("Mi")
            sleep(12610)
        elif magne < 81:
            radio.send("Ma")
            log.add({'Strength':magne})
            sleep(12610)     
    update()
