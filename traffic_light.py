
import time
import gpiozero

ledg = gpiozero.LED(4)
ledy = gpiozero.LED(16)
ledr = gpiozero.LED(21)


def traffic():
    ledg.on()
    time.sleep(2)
    ledg.off()
    ledy.on()
    time.sleep(2)
    ledy.off()
    ledr.on()
    time.sleep(2)
    ledr.off()


while True:
    traffic()
 
 
 


