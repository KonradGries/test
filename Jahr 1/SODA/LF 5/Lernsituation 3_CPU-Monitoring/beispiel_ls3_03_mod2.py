""" Beispiel_ls3_03_mod2

    Demo-Beispiel Module
    Das Beispiel wird wird genutzt, um den Umgang mit Modulen
    zu demonstrieren.
 
    Einordnung:			FISI-LF5-LS3-Beispiel-03
    Aufgabe: 			beispiel_ls3_03

    Name:               Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			04.12.2020
    Letzte Änderung:    12.01.2021        
    """

import beispiel_ls3_03_mod1 as mod1


def f0():
    """ Funktion f0 - Hauptfunktion, die andere nutzt """
    print("f0 - Start")
    mod1.f1()
    mod1.f2()
    print("f0 - Ende")


f0()
