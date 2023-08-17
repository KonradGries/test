import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT)
gpio.setup(38, gpio.IN)
gpio.setup(32, gpio.OUT)
gpio.setup(36, gpio.IN)
gpio.output(40, gpio.HIGH)

interrupt = 0

try:
    while 1:
        if gpio.input(38) == gpio.LOW:
            time.sleep(10)
        else:
            if gpio.input(36) == 0:
                gpio.output(40, gpio.LOW)
                gpio.output(32, gpio.HIGH)
                time.sleep(0.5)
                gpio.output(32, gpio.LOW)
                gpio.output(40, gpio.HIGH)
                time.sleep(0.5)
            else:
                gpio.output(40, gpio.HIGH)
                gpio.output(32, gpio.LOW)
                time.sleep(0.1)
            
except KeyboardInterrupt:
    pass
    #gpio.output(40, gpio.low)
gpio.output(40, gpio.HIGH)
gpio.cleanup()