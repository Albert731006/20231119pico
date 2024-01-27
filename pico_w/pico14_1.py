from machine import Timer,Pin,ADC
import time


def fun10(t:Timer | None = None):
    print('10秒了')
    led.toggle()

def fun10ms(t:Timer | None = None):
    print(light.read_u16())    

led = Pin(15, Pin.OUT)
light = ADC(Pin(28))
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer10ms = Timer(period=100, mode=Timer.PERIODIC, callback=fun10ms)
fun10()

    
