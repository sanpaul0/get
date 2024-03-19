import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

try:
    while True:
        c = input()
        a = int(c)
        GPIO.output(dac, decimal2binary(a))
        print(3.3*a/25)
except (TypeError, ValueError):
    if c == 'q':
        print('The program was stopped by keyboard')
        exit()
    else:
        print('Positive numbers only')
except RuntimeError:
    if a>255:
        print("Numbers less than 255 only")
except KeyboardInterrupt:
    print('The program was stopped by keyboard')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()



