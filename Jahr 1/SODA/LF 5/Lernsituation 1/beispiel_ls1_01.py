"""Beispiel_ls1_01

    Ein "Hallo-Welt-Skript"-Programm in der Sprache Python
 
    Einordnung:			FISI-LF5-LS1-Beispiel-01
    Aufgabe: 			beispiel_ls1_01

    Name:			    Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			04.04.2020
    Letzte Änderung:	26.12.2020       
    """

# benutzte Module importieren
import datetime
import os

# aktuelles Datum und Zeit holen
aktuellesDatum = datetime.datetime.now()
# Benutzernamen holen
benutzer = os.getlogin()

# Ausgabe
print("Hallo FISIs, hallo ITSEs")
print("Hallo " + benutzer)
print(aktuellesDatum.strftime("Datum: %d.%m.%Y"))
print(aktuellesDatum.strftime("Zeit:  %H:%M:%S"))
