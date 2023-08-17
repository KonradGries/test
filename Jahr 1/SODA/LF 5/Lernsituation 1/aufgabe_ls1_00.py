"""Aufgabe_ls1_00 - Ausgangsprogramm

    Python Programm zur Konvertierung zwischen verschiedenen Dateiformaten
    Ausgangsprogramm, welches in LS1 erweitert werden muss.
 
    Einordnung:         FISI-LF5-LS1-00
    Aufgabe:            aufgabe_ls1_00

    Name:               Markus Breuer
    Organisaion:        BK-GuT

    Erstellt:           07.04.2020
    Letzte Änderung:    20.08.2021
    """

# benötigte Module importieren
import sys
import os
import csv
import json

while 1:                                                                            # Endlosschleife
    # Programmüberschrift
    print("CSV-JSON-Konvertierer")
    print("---------------------")
    print("")
    # Menü und Benutzerauswahl
    print("(3) CSV -> JSON")
    print("(0) Ende")
    befehl = int(input("Auswahl: "))

    # Testen, ob ein bekannter Befehl eingegebn wurde
    if(befehl != 0 and befehl != 3):
        print("Unbekannter Befehl: " + str(befehl))
        continue

    if befehl == 0:                                                                 # Programm beenden
        print("Konvertierer beendet")
        break

    # Name der Eingabedatei
    nameEingabeDatei = input("Name Eingabedatei: ")
    # Name der Ausgabedatei
    nameAusgabeDatei = input("Name Ausgabedatei: ")

    # Testen, ob Eingabedatei existiert
    if os.path.isfile(nameEingabeDatei) != True:
        print("Eingabedatei: " + nameEingabeDatei + " nicht gefunden")
        continue

    if befehl == 3:                                                                 # CSV -> JSON
        print("Eingabedatei einlesen ...")
        # CSV-Datei öffnen
        csvdatei = open(nameEingabeDatei, "r", encoding="utf-8")
        reader = csv.DictReader(csvdatei, fieldnames=None)
        # Umwandeln
        print("In JSON-Format verwandeln ...")
        out = json.dumps([row for row in reader], indent=4, ensure_ascii=False)
        print("JSON-Datei erstellen ...")
        # JSON-Datei rausschreiben
        jsonDatei = open(nameAusgabeDatei, "w", encoding="utf-8")
        jsonDatei.write(out)
        jsonDatei.close()
        print("Konvertierung: CSV -> JSON")
        print("Ausgabedatei:  " + nameAusgabeDatei + " erfolgreich erstellt.")

    # Leerzeile für die Optik
    print("")

sys.exit(0)
