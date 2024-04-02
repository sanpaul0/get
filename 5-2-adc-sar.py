import RPi.GPIO as GPIO
import time as t

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def d2b(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]


def adc():
    c = 0
    for i in range(7,-1, -1):
        dac_value = d2b(c+ 2**i)
        GPIO.output(dac, dac_value)
        comp_value = GPIO.input(comp)
        t.sleep(0.1)
        if comp_value == 0:
            c += 2**i
    return c

    


try:
    while True:
        i = adc()
        voltage = 3.3 * i / 255.0
        print("{:.2f}V".format(voltage), i)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()