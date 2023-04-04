import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds=[21, 20, 16, 12, 7, 8, 25, 24]
#leds.reverse()
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, perev(k))
        sleep(0.005)
        if gpio.input(comp)==0:
            k-=2**i
    print("k = " + str(k))
    return k

def volume(n):
    n=int((n/45)*8)
    mas=[0]*8
    for i in range(n-1):
        mas[i]=1
    return mas

try:
    while True:
        k=adc()
        if k!=0:
            print("volume" + str(volume(k)))
            gpio.output(leds, volume(k))
            print(int(k/256*10))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
