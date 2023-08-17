""" beispiel_ls2_02a.py - Beispiel Matplotlib A - Erstellung einfacher Graphiken
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  07.02.2021, 07.07.2022
    """


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def liniendiagramm_1():
    """Zeichnen eines einfachen Liniendiagramms"""

    x_werte = np.array([0, 1, 2, 3, 4, 5, 6])  # Daten bereitstellen als gegebene Punkte
    y_werte = np.array([0, 250, 100, 125, 300, 250, 150])

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.plot(x_werte, y_werte)  # Graphen festlegen

    plt.show()


def liniendiagramm_2():
    """Zeichnen eines kompexeren Liniendiagramms"""

    x_werte = np.linspace(0, 12, 1000)  # Daten bereitstellen als Funktionen
    y1_werte = np.sin(x_werte)
    y2_werte = np.cos(x_werte)

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.plot(x_werte, y1_werte, label="Sinus")  # Graphen festlegen
    ax.plot(x_werte, y2_werte, label="Cosinus")

    ax.set_xlabel("X-Achse")  # Diagramm gestalten
    ax.set_ylabel("Y-Achse")
    ax.set_title("Komplexes Liniendiagramm")
    ax.legend(loc="upper left")
    ax.axhline(y=0.0, color="black", linestyle="-")  # 0-Linien hervorheben
    ax.axvline(x=0.0, color="black", linestyle="-")
    plt.show()


def balkendiagramm():
    """Zeichnen eines Balkendiagramms"""
    x_werte = np.array(
        ["Chrome", "Firefox", "Safari", "Edge", "Internet Explorer", "Opera"]
    )  # Daten bereitstellen
    y_werte = np.array([47.7, 23.1, 10.3, 7.8, 4.4, 3.9])

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.bar(x_werte, y_werte, align="center", color="green")  # Graphen festlegen

    ax.set_title("Balkendiagramm-Nutzung Web-Browser")
    ax.set_xlabel("Web-Browser")
    ax.set_ylabel("Prozentualer Anteil")
    plt.show()


def liniendiagramm_3():
    """Zeichnen eines Liniendiagramms, dessen Daten aus einer CSV-Datei stammen"""

    df = pd.read_csv("energiea.csv", sep=";")
    df.set_index("Energieträger", inplace=True)
    x_werte = list(df)  # Daten bereitstellen
    y_werte = df.loc["Steinkohle"]

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.plot(x_werte, y_werte, label="Steinkohle")  # Graphen festlegen

    ax.set_xlabel("Jahr")  # Diagramm gestalten
    ax.set_ylabel("PJ")
    ax.set_title("Primärenergie")
    ax.legend(loc="upper right")
    plt.show()


def hauptprogramm():
    """ Beispiel Matplotlib A - Hauptprogramm """
    liniendiagramm_1()
    liniendiagramm_2()
    balkendiagramm()
    liniendiagramm_3()


hauptprogramm()
