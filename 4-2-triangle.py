import RPi.GPIO as gpio
from time import sleep

dac = [26,19,13,6,5,11,9,10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(a,n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    while(True):
        triangle = input()
        if not triangle.isdigit():
            print("enter a number please")
        if (triangle.isdigit()):
            t = (int(triangle)/256) / 2
            if (int(triangle) < 0):
                print("please YOUR_NUMBER >= 0")
            for i in range(256):
                gpio.output(dac, dec2bin(i, 8))
                sleep(t)
            for i in range(255,-1,-1):
                gpio.output(dac, dec2bin(i, 8))
                sleep(t)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()