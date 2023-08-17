def modul():    #Wahl ob trigometrische Funktion oder Grundrechenarten ausgewählt werden soll
    modul_wahl = str(input ("Welche Rechenart wollen Sie benutzen? "))
    return modul_wahl

def untermodul():   #Wahl welcher Rechenoperator ausgewählt werden soll
    unter_modul_wahl = str(input ("Welche Grundrechenarten wollen Sie benutzen? "))
    return unter_modul_wahl

def eingabetri():   #Eingabefunktion für trigometrische Funktionen
    eingabetri = float(input("Welche Zahl wollen sie berechen lassen? "))
    return eingabetri

def zahl1():    #Eingabefunktion für zahl 1 der Grundrechenarten
    zahl1 = float(input("Erste Zahl eingeben "))
    return zahl1

def zahl2():    #Eingabefunktion für zahl 2 derGrundrechenarten
    zahl2 = float(input("Zweite Zahl eingeben "))
    return zahl2