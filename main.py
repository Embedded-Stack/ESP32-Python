import machine #type: ignore 
import time 
ldr = machine.ADC(machine.Pin(34)) 
ldr.atten(machine.ADC.ATTN_11DB) 
ldr.width(machine.ADC.WIDTH_10BIT) 
while True: 
     value = ldr.read() 
     print("&brightness& : ", 1023-value) 
     time.sleep(1) 
