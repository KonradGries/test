""" beispiel_ls2_02b.py - Beispiel Matplotlib B
                            - Basisgraphik
                            - Mehrer Funktionen in einem Diagramm
                            - Mehrer Subplots in einem Diagramm
                            - Optisches Aufpeppeln: Legenden, Beschriftungen, Achsen hervorheben
                            - Graphik speichern
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  06.04.2021, 07.07.2022
    """


import numpy as np  # NumPy und Matplotlib importieren
import matplotlib.pyplot as plt


def graphik_1():
    """Graphik 1 - Darstellung einer Sinus-Funktion im Bereich von 0 bis 10"""
    x_werte = np.linspace(0, 10, 100)  # x-Werte setzen
    y_werte = np.sin(x_werte)  # y-Werte berechnen

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.plot(x_werte, y_werte)  # Graphen festlegen

    ax.set_title("Graphik 1 - Sinusfunktion")  # Diagramm- und Achsentitel hinzufügen
    ax.set_xlabel("X-Achse")
    ax.set_ylabel("Y-Achse")

    plt.show()  # Graphik darstellen


def graphik_2():
    """Graphik 2 - Darstellung von Erlös-, Kosten- und Gewinnfunktion im Bereich von 0 bis 10"""
    x_werte = np.linspace(0, 10, 100)  # x- und y-Werte bestimmen als NumPy-Felder
    e_werte = 20 * x_werte  # Erlösfunktion
    k_werte = (
        np.power(x_werte, 3) - 10 * np.power(x_werte, 2) + 35 * x_werte + 18
    )  # Kostenfunktion
    g_werte = e_werte - k_werte  # Gewinnfunktion

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen

    ax.plot(x_werte, e_werte, label="Erlös")  # Graphen festlegen
    ax.plot(x_werte, k_werte, label="Kosten")
    ax.plot(x_werte, g_werte, label="Gewinn")

    ax.set_title(
        "Graphik 2 - Erlös-, Kosten- und Gewinnfunktion"
    )  # Diagramm- und Achsentitel hinzufügen
    ax.set_xlabel("ME")
    ax.set_ylabel("GE")
    ax.legend(loc="upper left")  # Legende anzeigen
    ax.grid(True)  # Raster einschalten
    ax.axhline(y=0.0, color="black", linestyle="-")  # 0-Linien hervorheben
    ax.axvline(x=0.0, color="black", linestyle="-")

    fig.savefig("graphik2.png")  # Graphik speichern

    plt.show()  # Graphik darstellen


def graphik_3():
    """Graphik 3 - Darstellung von 3 Subplots in einem Diagramm"""
    x_werte = np.linspace(0, 10, 100)  # x- und y-Werte bestimmen als NumPy-Felder
    e_werte = 20 * x_werte  # Erlösfunktion
    k_werte = (
        np.power(x_werte, 3) - 10 * np.power(x_werte, 2) + 35 * x_werte + 18
    )  # Kostenfunktion
    g_werte = e_werte - k_werte  # Gewinnfunktion

    fig, ax = plt.subplots(3, 1)  # Rahmen und Zeichenfächen erstellen

    ax[0].plot(x_werte, e_werte, label="Erlös")  # Graphen Zeichenbereich 1 festlegen
    ax[0].set_title("Graphik 3 - Erlös-, Kosten- und Gewinnfunktion")
    ax[0].set_ylabel("GE")
    ax[0].grid(True)
    ax[0].axhline(y=0.0, color="black", linestyle="-")
    ax[0].axvline(x=0.0, color="black", linestyle="-")
    ax[0].legend(loc="upper left")

    ax[1].plot(x_werte, k_werte, label="Kosten")  # Graphen Zeichenbereich 2 festlegen
    ax[1].set_ylabel("GE")
    ax[1].grid(True)
    ax[1].axhline(y=0.0, color="black", linestyle="-")
    ax[1].axvline(x=0.0, color="black", linestyle="-")
    ax[1].legend(loc="upper left")

    ax[2].plot(x_werte, g_werte, label="Gewinn")  # Graphen Zeichenbereich 3 festlegen
    ax[2].set_xlabel("ME")
    ax[2].set_ylabel("GE")
    ax[2].grid(True)
    ax[2].axhline(y=0.0, color="black", linestyle="-")
    ax[2].axvline(x=0.0, color="black", linestyle="-")
    ax[2].legend(loc="lower left")

    plt.show()  # Graphik darstellen


def beispiele():
    """Beispiel Matplotlib B - Hauptprogramm"""
    graphik_1()
    graphik_2()
    graphik_3()


beispiele()
