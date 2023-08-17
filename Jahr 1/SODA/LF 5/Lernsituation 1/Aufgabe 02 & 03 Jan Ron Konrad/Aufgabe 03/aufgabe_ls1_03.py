"""Aufgabe_ls1_00 - Ausgangsprogramm

    Python Programm zur Konvertierung zwischen verschiedenen Dateiformaten
    Ausgangsprogramm, welches in LS1 erweitert werden muss.
 
    Einordnung:         FISI-LF5-LS1-03
    Aufgabe:            aufgabe_ls1_03

    Name:               Markus Breuer
    Organisaion:        BK-GuT

    Erstellt:           07.04.2020
    Letzte Änderung:    20.08.2021
    https://www.python-lernen.de/python-modul-time.

    Erweitert von Jan Mix, Ron Schröter, Konrad Gries
    am 21.11.2021

    """

# benötigte Module importieren
import sys
import os
import csv
import json
import time



# Endlosschleife starten
while 1:   

    # Programmüberschrift
    print("CSV-JSON-Konvertierer")
    print("---------------------")
    print("")

    # Menü und Benutzerauswahl
    print("(1) CSV Datei anzeigen") 
    print("(2) JSON Datei anzeigen") 
    print("(3) CSV -> JSON")
    print("(4) JSON -> CSV")
    print("(0) Ende")

    #Benutzereingabe
    befehl = int(input("Auswahl: "))


    # Testen, ob ein bekannter Befehl eingegebn wurde
    if(befehl != 0 and befehl !=3 and befehl !=1 and befehl !=2 and befehl !=4):
        print("Unbekannter Befehl: " + str(befehl))
        print("Erneute Eingabe")
        print("")
        continue
    #Programm beenden    
    if befehl == 0:                                                                
        print("Konvertierer beendet")
        break


    # Name der Eingabedatei eingeben 
    nameEingabeDatei = input("Name Eingabedatei: ")
   
    # Testen, ob Eingabedatei existiert
    if os.path.isfile(nameEingabeDatei) != True:
        print("Eingabedatei: " + nameEingabeDatei + " nicht gefunden")
        continue



    #Befehl 1: Anzeigen von Csv Datei
    if befehl == 1:
        print("")
        file = open(nameEingabeDatei, "r", encoding="utf-8")
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(', '.join(row))
        print ("")    
        file.close()    
        continue



    #Befehl 2: Anzigen von Jsondatei
    if befehl == 2:
        print("")
        file  = open(nameEingabeDatei, "r", encoding="utf-8")
        data = json.load(file)
        print (json.dumps(data ,indent = "\t"))
        print ("")
        file.close()
        continue

    

    #Befehl 3: Konventierung von Csv in Json   
    if befehl == 3:  

        # Name der Ausgabedatei eingeben und beginnen Zeit zu messen
        nameAusgabeDatei = input("Name Ausgabedatei: ")
        start_time = time.time()                                                            # CSV -> JSON
        print("Eingabedatei einlesen ...")

        # CSV-Datei öffnen
        csvdatei = open(nameEingabeDatei, "r", encoding="utf-8") 
        reader = csv.DictReader(csvdatei, fieldnames=None)

        # Umwandeln
        print("In JSON-Format umwandeln ...")
        out = json.dumps([row for row in reader], indent=4, ensure_ascii=False)
        print("JSON-Datei erstellen ...")

        # JSON-Datei rausschreiben
        jsonDatei = open(nameAusgabeDatei, "w", encoding="utf-8")
        jsonDatei.write(out)
        jsonDatei.close()
        print ("")
        print("Konvertierung: CSV -> JSON")
        print("Ausgabedatei:  " + nameAusgabeDatei + " erfolgreich erstellt.")


        #Zeitmessung
        zeit =round ( float( time.time() - start_time ) ,4 )
        count=-1
        with open (nameEingabeDatei,'rb') as f:
          for line in f:
             count+=1
        print (str(count) + " Datensätze")
        print (str(zeit) + " Sekunden")
        print ("")
        continue



    #Befehl 4: Konventieren von Json in CSV
    # Für Befehl vier die Datei jsondatei.json benutzen da wir keine allgemeine Version für alle JSON-Dateien hinbekommen haben
    if befehl == 4: 

        # Name der Ausgabedatei eingeben und beginnen Zeit zu messen
        nameAusgabeDatei = input("Name Ausgabedatei: ")
        start_time = time.time()                                                         
        print("Eingabedatei einlesen ...")

        # Json-Datei öffnen
        with open (nameEingabeDatei , "r", encoding="utf-8") as jsondatei:
           data =json.load(jsondatei)
           csvdata = data["List"]

        # CSV Datei erstellen und die Daten reinschreiben
        print("CSV-Datei erstellen ...")
        with open (nameAusgabeDatei, "w",encoding="utf-8",newline="") as csvdatei:
            fieldnames =csvdata[0].keys()
            writer = csv.DictWriter(csvdatei, fieldnames=fieldnames)
            writer.writeheader()
            for names in csvdata:
                writer.writerow(names)
        print ("")
        print("Konvertierung: JSON -> CSV")
        print("Ausgabedatei:  " + nameAusgabeDatei + " erfolgreich erstellt.")

        #Zeitmessung und Datensätze
        zeit =round ( float( time.time() - start_time ) ,4 )
        count=-1
        with open (nameEingabeDatei,'rb') as f:
          for line in f:
             count+=1
        print ( str(count) + " Datensätze")
        print (str (zeit) + " Sekunden")

    # Leerzeile für die Optik
    print("")
  

sys.exit(0)
