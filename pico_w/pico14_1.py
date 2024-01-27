from machine import Timer,Pin


def fun10(t:Timer | None = None):
    print('10秒了')
    led.toggle()

led = Pin(15, Pin.OUT)
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
fun10()


while True:
    pass
