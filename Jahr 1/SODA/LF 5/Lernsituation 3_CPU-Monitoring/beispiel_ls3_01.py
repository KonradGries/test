"""Beispiel_ls3_01 - Datenbanknutzung

    Ein Beispielprogramm, welches das Zusammenspiel von Python mit
    MariaDB demonstriert.
 
    Einordnung:			FISI-LF5-LS3-Beispiel-01
    Aufgabe: 			beispiel_ls3_01

    Name:			    Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			14.04.2020
    Letzte Änderung:	01.01.2021     
    """

import mysql.connector
from random import random

print("Verbindung zur Datenbank aufbauen")
print("")

connection = mysql.connector.connect(
    host="localhost",
    port=3306,  # Verbindung zur Datenbank aufbauen
    user="root",
    passwd="",
    db="beispiel_ls3_01",
)

cursor = connection.cursor()  # Cursor zum Ausführen von SQL-Statements erstellen


print("50 Werte in Datenbank schreiben")
i = 1
while i <= 50:
    wert = random() * 100
    wert = round(wert, 2)
    sqlStatement = "INSERT INTO t1_demo ( t1_wert) VALUES ( " + str(wert) + ")"
    cursor.execute(sqlStatement)
    connection.commit()
    i = i + 1
print("")

cursor.execute("SELECT * FROM t1_demo")  # SQL-Befehl ausführen

print("Tabelleninhalt ausgeben:")
print("------------------------")
print("")
print(" Nr : Zeitpunkt : Wert")

result = cursor.fetchall()  # Ergebnismenge abholen
for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
    print(str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]))

print("")

cursor.close()  # Cursor schliessen

print("Verbindung zur Datenbank abbauen")
print("")

connection.close()  # Verbindung zur Datenbank abbauen
