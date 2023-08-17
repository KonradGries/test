"""Beispiel_ls1_02

    Ein Zählprogramm-Programm in der Sprache Python
    !!! Die Einrückung bestimmt die Struktur !!!
 
    Einordnung:			FISI-LF5-LS1-Beispiel-01
    Aufgabe: 			beispiel_ls1_01

    Name:			    Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			27.08.2020
    Letzte Änderung:	      
    """

# Überschrift ausgeben
print("Zählprogramm")
print("------------")
print("")

# Zählrichtung abfragen
richtung = int(input("1 - Vorwärts, 2 - Rückwärts : "))
print("")


if richtung == 1:  # Vorwärts zählen
    i = 1
    while i <= 10:
        print(i)
        i = i + 1
elif richtung == 2:  # Rückwärts zählen
    i = 10
    while i >= 1:
        print(i)
        i = i - 1
else:  # Unbekannter Befehl -> Fehlermeldung
    print("Unbekannte Eingabe")
