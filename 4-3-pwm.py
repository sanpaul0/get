import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
p = GPIO.PWM(21, 1000)
p.start(0)
try:
    while True:
        dc = int(input())
        p.ChangeDutyCycle(dc)
        print(3.3*dc/100)
finally:
    p.stop()
    GPIO.output(27, 0)
    GPIO.cleanup()