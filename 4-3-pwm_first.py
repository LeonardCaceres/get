import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT)

p = GPIO.PWM(24, 10)
p.start(50)
input('Press return to stop: ')
p.stop()
GPIO.cleanup()