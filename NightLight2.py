from machine import PWM, Pin #type: ignore
from time import sleep

led = PWM(Pin(2))
button = Pin(32, Pin.IN, Pin.PULL_UP)
led.freq(1000)
status = False
while True:
    pressed = button.value()
    while button.value() == 0:
        sleep(0.01)
    if pressed == 0:
        print("Button Pressed")
        status = not status
        sleep(0.25)
    if status == 1:
        print("Blinking")
        for i in range(1023, 0, -50):
            led.duty(i)
            sleep(0.05)
        for i in range(0, 1024, 50):
            led.duty(i)
            sleep(0.05)
    else:
        led.duty(0)