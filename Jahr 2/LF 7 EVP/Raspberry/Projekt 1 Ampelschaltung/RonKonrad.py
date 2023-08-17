import RPi.GPIO as gpio #Importiert die Rpi.GPIO Library unter dem Alias "gpio"
import time             #Importiert die time Library

#Setzt das Schaltbrett in den Boardmodus für die richtige Nummerierung der Pins 
gpio.setmode(gpio.BOARD)

#Definiert die Ein(IN)- und Ausgänge(OUT):
gpio.setup(36, gpio.OUT)
gpio.setup(38, gpio.OUT)
gpio.setup(40, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.IN)

#36 = Autoampel Rot
#38 = Autoampel Gelb
#40 = Autoampel Grün
#16 = Fußgängerampel Rot
#18 = Fußgängerampel Grün
#22 = Taster

for i in range(1000):                   #Eine for-Schleife, die 1000 mal durchläuft
    gpio.output(40, gpio.HIGH)          #Setzt Autoampel auf Grün
    gpio.output(16, gpio.HIGH)          #Setzt Fußgängerampel auf Rot
    if gpio.input(22) == gpio.LOW:      #Wenn der Taster gedrückt wird startet die Fußgängerampel
        gpio.output(40, gpio.LOW)       #Autoampel wechselt von Grün auf Gelb
        gpio.output(38, gpio.HIGH)
        time.sleep(1)                   #Zustand wird für 1 Sekunde beibehalten
        gpio.output(38, gpio.LOW)       #Autoampel wechselt von Gelb zu Rot
        gpio.output(36, gpio.HIGH)
        time.sleep(1)                   #Zustand wird für 1 Sekunde beibehalten
        gpio.output(16, gpio.LOW)       #Fußgängerampel springt von Rot auf Grün
        gpio.output(18, gpio.HIGH)      
        time.sleep(3)                   #Zustand wird für 3 Sekunde beibehalten
        gpio.output(18, gpio.LOW)       #Fußgängerampel springt Grün auf Rot
        gpio.output(16, gpio.HIGH)
        time.sleep(1)                   #Zustand wird für 1 Sekunde beibehalten
        gpio.output(38, gpio.HIGH)      #Bei der Autoampel wird nun auch die Gelbe Leuchte angeschaltet
        time.sleep(1)                   #Zustand wird für 1 Sekunde beibehalten
        gpio.output(36, gpio.LOW)       #Gelb und Rot werden bei der Autoampel ausgeschaltet und Grün angeschaltet
        gpio.output(38, gpio.LOW)
        gpio.output(40, gpio.HIGH)
    else:
        time.sleep(0.01)                #Falls der Taster nicht gedrückt wird wartet das Programm für 10 Millisekunden, dannach startet die Schleife von vorne und durchläuft diese für 10 Sekunden
        
gpio.cleanup()  #Nach Abschluss der Schleife werden die gesetzten Gpio Pins zurückgesetzt