import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)
leds = [2, 3, 4 , 17, 27, 22, 10,9]
GPIO.setup(leds , GPIO.OUT)
for i in range(3):
    for j in range(len(leds)):
        GPIO.output(leds[j], 1)
        time.sleep(0.2)
        GPIO.output(leds[j], 0)
GPIO.output(leds, 0)
time.sleep(1)
GPIO.cleanup()