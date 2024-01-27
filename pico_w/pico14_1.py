from machine import Timer,Pin,ADC
import time


def fun10(t:Timer | None = None):
    print('10秒了')
    led.toggle()

def fun500ms(t:Timer | None = None):
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')

led = Pin(15, Pin.OUT)
light = ADC(Pin(28))
vr = ADC(Pin(27))
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)
fun10()

    
