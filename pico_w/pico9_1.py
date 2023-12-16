import time
from machine import Pin

led=Pin("LED",Pin.OUT)

while True:
    led.high()
    time.sleep(1)
    led.low()
    time.sleep(1)
    