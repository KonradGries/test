"""Aufgabe_ls3_01 - Ausgangsprogramm

    Ein Beispielprogramm, welches das Zusammenspiel von Python mit
    MySQL demonstriert.

    Ausgangsprogramm

    Einordnung:			FISI-LF5-LS3-Aufgabe-ls3-00
    Aufgabe: 			aufgabe_ls3_00

    Name:			    Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			14.04.2020
    Letzte Änderung:    26.01.2021
    """

import mysql.connector
import dblib as lib
from time import sleep
import psutil
import export 

### lokale Funktionen für die Datenbanknutzung ###########################################################

def dbZugriffswerte():
    """ Funktion, die die Zugriffsdaten für eine MySQL-Datenbank liefert """
    return "localhost", "root", "", "aufgabe_ls3_01"


### Hauptprogramm ###################################################################################

# Verbindung zur Datenbank aufbauen
print("Verbindung zur Datenbank aufbauen")
print("")
host, user, passwd, db = dbZugriffswerte()
connection = lib.dbVerbindungAufbauen(host, user, passwd, db)

print ("Wie oft soll die Cpuauslastung gespeichert werden?")
intervall = int(input("Intervallanzahl in ganzen Zahlen: "))
periode = int(input("Zeit zwichen den einzelnen Messungen in Sekunden: "))

# Werte in Datenbank schreiben
print("Es werden" , intervall , "Werte in Datenbank schreiben, alle" , periode , "Sekunden")
i = 1
while i <= intervall:
    wert = psutil.cpu_percent()
    sqlStatement = "INSERT INTO cpu_log ( t1_wert) VALUES ( " + str(wert) + ")"
    lib.dbNichtAbfrageAnweisung(connection, sqlStatement)
    sleep(periode)
    i = i + 1
print("")

# Tabelleninhalt ausgeben
print("Tabelleninhalt ausgeben:")
print("------------------------")
print("")
print(" Nr : Zeitpunkt : Wert")
result = lib.dbAbfrageAnweisung(connection, "SELECT * FROM cpu_log ")
for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
    print(str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]))

auswahl = str(input("Möchtest du die Daten in eine CSV ausgeben? "))
if auswahl == "Ja":
    result = lib.dbAbfrageAnweisung(connection, "SELECT * FROM cpu_log ")
    for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
        (str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]))
else :
    print ("")    

print("")

# Verbindung zur Datenbank abbauen
print("Verbindung zur Datenbank abbauen")
print("")
lib.dbVerbindungAbbauen(connection)