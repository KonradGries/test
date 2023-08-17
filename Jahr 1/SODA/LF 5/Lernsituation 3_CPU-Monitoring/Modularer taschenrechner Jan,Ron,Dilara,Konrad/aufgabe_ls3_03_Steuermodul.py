import aufgabe_ls3_03_tri as trigo  #Import von den anderen Modulen
import aufgabe_ls3_03_Grund as grund
import aufgabe_ls3_03_Benutzerinteraktion as ben
programm_laufend = 1

while programm_laufend == 1:    #Fortlaufende Schleife für das Programm

    print ("")
    print ("Welche Rechenart wollen Sie benutzen?" )
    print ("Geben Sie für Grundrechenarten grund ein oder für trigonometrische Funktion trigo ein.")
    print ("Zum Beenden des Programmes geben Sie exit ein.")
    print ("")

    modul_wahl = ben.modul() 


    if modul_wahl == "grund":   #Teil zum Berechen der Grundrechenarten
        print ("Welche Grundrechenarten wollen Sie benutzen?")
        print ("Sie haben die folgenden Wahlmöglichkeiten -> plus, minus, mal, geteilt.")

        unter_modul_wahl = ben.untermodul()
        zahl1 = ben.zahl1()
        zahl2 = ben.zahl2()
        #Bei Wahl der folgenden Operatoren werden diese mit den beiden Zahlen berechnet
        if unter_modul_wahl == "plus":
            ergebnis =   grund.plus(zahl1,zahl2)

        elif unter_modul_wahl == "minus":
            ergebnis =   grund.minus(zahl1,zahl2)

        elif unter_modul_wahl == "mal":
            ergebnis =   grund.mal(zahl1,zahl2)

        elif unter_modul_wahl == "geteilt":
            ergebnis =   grund.geteilt(zahl1,zahl2)

        print ("Das Ergebnis lautet:")
        print (ergebnis)    #Ausgabe des Ergebisses


    elif modul_wahl == "trigo":    #Teil zum berechnen der trigometrischen Funktionen
        print ("Welche trigonometrische Funktion wollen Sie benutzen?")
        print ("Sie haben die folgenden Wahlmöglichkeiten -> sin, cos, tan, asin, acos, atan.")

        unter_modul_wahl = ben.untermodul()        
        eingabetri = ben.eingabetri()
        #Bei Wahl der folgenden Operatoren werden diese berechnet
        if unter_modul_wahl == "sin":
            ergebnistri = trigo.Berechnesinus(eingabetri)

        elif unter_modul_wahl == "cos":
            ergebnistri = trigo.Berechnecosinus(eingabetri)

        elif unter_modul_wahl == "tan":
            ergebnistri = trigo.Berechnetangens(eingabetri)

        elif unter_modul_wahl == "asin":
            ergebnistri = trigo.Berechnearcsinus(eingabetri)

        elif unter_modul_wahl == "acos":
            ergebnistri = trigo.Berechnearccosinus(eingabetri)

        elif unter_modul_wahl == "atan":
            ergebnistri = trigo.Berechnearctangens(eingabetri)

        print ("Das Ergebnis lautet:")
        print (ergebnistri)    #Ausgabe des Ergebnisses
       
        
    elif modul_wahl == "exit":  #Abbruch des Programms
        exit()