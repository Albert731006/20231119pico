import time
from machine import Pin

led=Pin("LED",Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    