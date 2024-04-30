import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
import numpy as np

troyka = 13
comp = 14
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def d2b(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]


def adc():
    for i in range(256):
        dac_value = d2b(i)
        GPIO.output(dac, dac_value)
        comp_value = GPIO.input(comp)
        
        if comp_value:
            return i
    return 255

def adc_1():
    l = 0
    for i in range(7, -1, -1):
        l+=2**i
        GPIO.output(dac, d2b(l))
        time.sleep(0.002)
        comp_value = GPIO.input(comp)
        if comp_value != 0:
            l -= 2**i
    return l

def num2leds(val):
    GPIO.output(dac, d2b(val))
    return d2b(val)

t = []
V = []
GPIO.output(troyka, 0)

try:
    GPIO.output(troyka,1)
    st = time.time()
    val = 0
    while (val < 242):
        val = adc_1()
        print(val)
        V.append(val/255*3.3)
        t.append(time.time() - st)
    GPIO.output(troyka, 0)
    while (val > 24):
        val = adc_1()
        print(val)
        V.append(val/255*3.3)
        t.append(time.time() - st)
    ft = time.time()

    
    a = 3.3/255

    with open('data.txt', 'w') as f:
        for i in range(len(V)):
            f.write(str(V[i])+ "\n")
        f.close

    with open('settings.txt', 'w') as g:
        g.write('средняя частоту дискретизации:' + str(len(V)/t[-1]) + "\n") 
        g.write('шаг квантования АЦП: ' + str(a))
        g.close

    print(ft - st , 'с - время эксперимента' )
    print(t[-1]/len(V), 'c - период одного измерения')
    print(len(V)/t[-1], 'Гц - частота дискретизации')
    print(a, 'В - шаг квантования АЦП')
    fig = plt.figure(figsize = (16,9))
    ax1 = fig.add_subplot(111)
    u = np.array(t)
    v = np.array(V)
    ax1.scatter(u,v,marker = '.')
    #ax1.plot(u, v, 'k')
    ax1.grid
    plt.show()
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()