import RPi.GPIO as GPIO
import time as time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(val):
    
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

try:
    period = float(input())
    while True:
        for i in range(255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period/512)
        for i in range(255, 0, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
