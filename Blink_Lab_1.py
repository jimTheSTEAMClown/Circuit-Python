#import time
from time import sleep
from adafruit_circuitplayground import cp

print("Hello <Your Name>") 
while True:
    cp.red_led = True
    sleep(0.5)
    cp.red_led = False
    sleep(0.5)
