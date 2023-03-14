from microbit import *
import music
import radio
import log
radio.config(group=4)
radio.on()

while True:
    
    message=radio.receive()
    if message == "Mi":
        log.add({'Scenario':message})
        for i in range(1,5):
            music.play(['d', 'a'])
        music.stop()
        display.scroll('Noise. Noise.')
    elif message == "Ma":
        log.add({'Scenario':message})
        for i in range(1,5):
            music.play(['c', 'g'])
        music.stop()
        display.scroll('Door. Door')
