""" Beispiel_ls3_02

    Demo-Beispiel Funktionen
    Das Beispiel wird wird genutzt, um den Umgang mit Funktionen
    zu demonstrieren.

    Einordnung:         FISI-LF5-LS3-Beispiel-02
    Aufgabe:            beispiel_ls3_02

    Name:               Markus Breuer
    Organisaion:        BK-GuT

    Erstellt:           24.11.2020
    Letzte Änderung:    03.01.2022
    """


# Definition f1 - f1 zählt von 0 bis n
def f1(n):
    """ Funktion f1 - Funktion, die bis n zählt und nichts zurückgibt """
    i = 0
    while i <= n:
        print(i)
        i = i + 1
    print("")
    return


# Aufrufe von f1
f1(5)
z = int(input("Wie weit soll ich zählen? "))
f1(z)


# Definition f2 - f2 berechnet das Volumen einer Quaders
def f2(l=5, b=5, h=5):
    """ Funktion f2 - berechnet Volumen eines Quaders und gibt dieses zurück """
    v = l * b * h
    return v


# Aufrufe von f2
vol = f2(10, 10, 5)  # Aufruf mit allen Parametern
print("Volumen bei Aufruf von 'f2( 10, 10, 5)':", vol)
vol = f2()  # Aufruf ohne Parameter
print("Volumen bei Aufruf von 'f2()':", vol)
vol = f2(1, 1)  # Aufruf mit 2 von 3 Parametern
print("Volumen bei Aufruf von 'f2( 1, 1)':", vol)
vol = f2(h=7)  # Aufruf mit benamten Parametern
print("Volumen bei Aufruf von 'f2( h = 7)':", vol)
print("")


# Definition f3 - f1 zählt von 0 bis n und gibt dies als Liste zurück
def f3(n):
    """ Funktion f3 - gibt eine Liste zurück """
    liste_lokal = []
    i = 0
    while i <= n:
        liste_lokal.append(i)
        i = i + 1
    return liste_lokal


# Aufruf von f3
liste_global = f3(5)
print("Liste:", liste_global)
print("")


# Definition weiterer Funktionen, die ein ganzes Geflecht bilden
def f4a():
    """ Funktion f4a """
    print("f4a - Start")
    print("f4a - Ende")


def f4b():
    """ Funktion f4a """
    print("f4b - Start")
    f4c()
    print("f4b - Ende")


def f4c():
    """ Funktion f4a """
    print("f4c - Start")
    print("f4c - Ende")


def f4():
    """ Funktion f4a """
    print("f4 - Start")
    f4a()
    f4b()
    print("f4 - Ende")


f4()
print("")
