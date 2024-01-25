from machine import Pin

red_led = Pin(15,mode=Pin.OUT)
red_led.value(0)