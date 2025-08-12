from machine import Pin, Timer #type: ignore

led = Pin(2, Pin.OUT)

def blink(timer):
    led.value(not led.value())

tim = Timer(0)
tim.init(period=10000, mode=Timer.PERIODIC, callback=blink)