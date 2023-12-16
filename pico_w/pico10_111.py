from machine import ADC,Timer
import time

def alarm():
    print("要爆炸了")
def callback1(t:Timer):
    global start
    sensor = ADC(4)
    vol = sensor.read_u16()*(3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    if temperature >=27 and delta >= 60 * 1000:
        alarm()
        start = time.ticks_ms()
        
start = time.ticks_ms() - (60 * 1000)

time1 = Timer()
time1.init(period=1000,callback=callback1)
