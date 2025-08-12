from  machine import Pin, PWM #type: ignore
import time
 
status = False
led = PWM(Pin(2))
button = Pin(32, Pin.IN, Pin.PULL_UP)
led.freq(500)

def fade():
    for i in range(0, 1023, 50):
        led.duty(i)
        time.sleep(0.05)
    for i in range(1023, 0, -50):
        led.duty(i)
        time.sleep(0.05)

def readButton():
    global status
    if status == True:
        status = False
    else:
        status = True
    time.sleep(0.2)

while True:
    if button.value()== 0:
        print("BUTTON PRESSED")
        while button.value() == 0:
            time.sleep(0.01)
        readButton()
    if status:
        print("FADING...")
        fade()
    else:
        #print("TURNING OFF...")
        led.duty(0)
