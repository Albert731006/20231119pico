from machine import ADC,Timer

def alarm():
    print("要爆炸了")
def callback1(t:Timer):
    sensor = ADC(4)
    vol=sensor.read_u16()*(3.3/65535)
    temperature=27-(vol-0.706) / 0.001721
    print(temperature)
    if temperature >=28:
        alarm() 

time1 = Timer()
time1.init(period=1000,callback=callback1)
