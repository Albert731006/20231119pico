from machine import Timer
from machine import Pin

def callback1(t):
    p25 = Pin("LED", Pin.OUT)
    p25.on()
def callback2(t):
    p25 = Pin("LED", Pin.OUT)
    p25.off()    

time1 = Timer()
time1.init(freq=1,callback=callback1)

time2 = Timer()
time2.init(period=2500,callback=callback2)




