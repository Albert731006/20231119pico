from machine import Timer,Pin,ADC
import time


def fun10(t:Timer | None = None):
    print('10秒了')
    led.toggle()

def fun500ms(t:Timer | None = None):
    print(light.read_u16())    

led = Pin(15, Pin.OUT)
light = ADC(Pin(28))
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)
fun10()

    
