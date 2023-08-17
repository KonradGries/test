import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)


p = GPIO.PWM(32, 100) #Pin und Hertzfrequenz
dc=0
p.start(dc)


try:
    while True:
        for dc in range(50, 101, 5): #Schleife mit Startwert, Endwert und interval
            p.ChangeDutyCycle(dc)
            time.sleep(0.2)
            
        for dc in range(100, 50, -5): #Schleife mit Startwert, Endwert und interval
            p.ChangeDutyCycle(dc)
            time.sleep(0.2)
            
except KeyboardInterrupt:# mit strg + c stop
    print("stop")

p.stop()
GPIO.cleanup()
#JP ist ein super leherer