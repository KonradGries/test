print ("Temperaturumwandler \n")
einheit = str (input ("In welche Einheit möchten sie umwandeln? (C/F) "))
temp = 0
if einheit == "F":
    temp = float (input ("Geben sie die Temperatur in Celsius ein: "))
    umrechnung = temp * 9/5 + 32
    print (umrechnung) 
elif einheit == "C":
    temp = float (input ("Geben sie die Temperatur in Fahrenheit ein: "))
    umrechnung = (temp - 32) * (5/9)
    print (umrechnung) 
else:
    print ("Fehler")