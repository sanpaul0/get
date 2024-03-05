import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)
leds = [2, 3, 4 , 17, 27, 22, 10,9]
aux = [21,20,26,16,19,25,23,24]
GPIO.setup(leds , GPIO.OUT)
GPIO.setup(aux , GPIO.IN)
while True:
    for i in range(8):
        a = GPIO.input(aux[i])
        GPIO.output(leds[i], a)
        