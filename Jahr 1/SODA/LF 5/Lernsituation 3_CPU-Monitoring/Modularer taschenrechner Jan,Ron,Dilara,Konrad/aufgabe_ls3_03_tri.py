import math    #Importieren von Math Modul zum berechenn der Funktionen

def Berechnesinus(eingabetri):                  #Funktion zum Berechnen von Sinus
    ausgabetri = math.sin(eingabetri)           #Berechnung der Funktion
    return ausgabetri                           #Rückgabe des Ergebnisses

def Berechnecosinus(eingabetri):                #Wiederholung des gleichen Prinzipes bei den restlichen Funktionen nur mit Änderung der Rechenoperation
    ausgabetri = math.cos(eingabetri)
    return ausgabetri

def Berechnetangens(eingabetri):
    ausgabetri = math.tan(eingabetri)
    return ausgabetri 

def Berechnearcsinus(eingabetri):
    ausgabetri = math.asin(eingabetri)
    return ausgabetri 

def Berechnearccosinus(eingabetri):
    ausgabetri = math.acos(eingabetri)
    return ausgabetri 

def Berechnearctangens(eingabetri):
    ausgabetri = math.atan(eingabetri)
    return ausgabetri 