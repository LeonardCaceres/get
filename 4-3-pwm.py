import RPi.GPIO as gpio
from time import sleep
#import sys

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)

dac = [26,19,13,6,5,11,9,10]

gpio.setup(dac, gpio.OUT,initial = gpio.HIGH)
pwm = gpio.PWM(2,1000)
pwm.start(0)

def dec2bin(a,n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

t = 10
try:
    while(True):
        DutyCircle = int(input('print %[0 - 100]: '))
        if DutyCircle >= 0 and DutyCircle <=100:
            pwm.ChangeDutyCycle(DutyCircle)
            print("{:.2f}".format(DutyCircle*3.3 / 100))
            sleep(t)
        else:
            print("Please print %\n")
finally:
    gpio.output(dac, 0)
    gpio.output(2, 0)
    gpio.cleanup()