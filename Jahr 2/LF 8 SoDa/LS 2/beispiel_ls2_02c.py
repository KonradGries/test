""" beispiel_ls2_02c.py - Beispiel Matplotlib C
                            - Histogramm
                            - Säulendiagramm
                            - Balkendiagramm
                            - Kuchendiagramm
                            - Streudiagramm
                            - Boxplot-Diagramm
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  07.04.2021, 07.07.2022
    """


import numpy as np
import matplotlib.pyplot as plt


def graphik_1():
    """Graphik 1 - Darstellung eines Histogramms"""
    # x-Werte bestimmen, 10.000 Werte Standardverteilung
    mu = 175
    sigma = 10
    x_werte = mu + sigma * np.random.randn(10000)

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.hist(x_werte, 20, density=True, facecolor="blue")  # Graphen festlegen

    # Diagramm- und Achsentitel hinzufügen
    ax.set_title("Graphik 1 - Darstellung eines Histogramms")
    ax.set_xlabel("Größe")
    ax.set_ylabel("Wahrscheinlichkeit")
    ax.grid(True)  # Raster einschalten
    ax.text(140, 0.03, "µ=175 s=10")

    plt.show()  # Graphik darstellen


def graphik_2():
    """Graphik 2 - Darstellung eines Säulendiagramms"""
    # Daten festlegen
    fluss = [
        "Nil",
        "Amazonas",
        "Jangtsekiang",
        "Missisippi",
        "Jenissei",
    ]
    laenge = [6650, 6400, 6380, 6051, 5540]

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.bar(fluss, laenge, color="blue")  # Graphen festlegen

    # Diagramm- und Achsentitel hinzufügen
    ax.set_title("Graphik 2 - Darstellung eines Säulendiagramms")
    ax.set_xlabel("Fluss")
    ax.set_ylabel("Länge(km)")

    plt.show()  # Graphik darstellen


def graphik_3():
    """Graphik 3 - Darstellung eines Balkendiagramms"""
    # Daten festlegen
    fluss = [
        "Nil",
        "Amazonas",
        "Jangtsekiang",
        "Missisippi",
        "Jenissei",
    ]
    laenge = [6650, 6400, 6380, 6051, 5540]

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.barh(fluss, laenge, color="blue")  # Graphen festlegen

    # Diagramm- und Achsentitel hinzufügen
    ax.set_title("Graphik 3 - Darstellung eines Balkendiagramms")
    ax.set_ylabel("Fluss")
    ax.set_xlabel("Länge(km)")

    plt.show()  # Graphik darstellen


def graphik_4():
    """Graphik 4 - Darstellung eines Kuchendiagramms"""
    # Daten festlegen
    kontinent = [
        "Asien",
        "Afrika",
        "Europa",
        "Südamerika",
        "Nordamerika",
        "Australien/Ozianien",
    ]
    bevoelkerungsanteil = [59.51, 17.21, 9.61, 8.38, 4.73, 0.55]

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.pie(bevoelkerungsanteil, labels=kontinent, autopct="%.2f%%")  # Graphen festlegen

    # Diagramm- und Achsentitel hinzufügen
    ax.set_title("Graphik 4 - Darstellung eines Kuchendiagramms")

    plt.show()  # Graphik darstellen


def graphik_5():
    """Graphik 5 - Darstellung eines Streudiagramms"""
    # x-Werte bestimmen, 100 Werte Standardverteilung
    mu1 = 180
    sigma1 = 5
    x_werte = mu1 + sigma1 * np.random.randn(100)

    # y-Werte bestimmen, 100 Werte Standardverteilung
    mu2 = 80
    sigma2 = 10
    y_werte = mu2 + sigma2 * np.random.randn(100)

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.scatter(x_werte, y_werte)  # Graphen festlegen

    # Diagramm- und Achsentitel hinzufügen
    ax.set_title("Graphik 5 - Darstellung eines Streudiagramms")
    ax.set_xlabel("Größe (cm)")
    ax.set_ylabel("Gewicht (kg)")
    ax.grid(True)  # Raster einschalten

    plt.show()  # Graphik darstellen


def graphik_6():
    """Graphik 6 - Darstellung eines Boxplot-Diagramms"""
    # x-Werte bestimmen, jeweils 100 Werte Standardverteilung
    x_werte_1 = np.random.normal(180, 5, 100)
    x_werte_2 = np.random.normal(175, 10, 100)
    x_werte_3 = np.random.normal(190, 2, 100)
    x_werte_4 = np.random.normal(180, 5, 100)
    x_werte_5 = np.random.normal(185, 5, 100)
    x_werte = [x_werte_1, x_werte_2, x_werte_3, x_werte_4, x_werte_5]

    beschriftung = ["Gruppe 1", "Gruppe 2", "Gruppe 3", "Gruppe 4", "Gruppe 5"]

    fig, ax = plt.subplots()  # Rahmen und Zeichenfäche erstellen
    ax.boxplot(x_werte)  # Graphen festlegen

    # Diagramm- und Achsentitel hinzufügen
    ax.set_title("Graphik 6 - Darstellung eines Boxplot-Diagramms")
    ax.set_ylabel("Größe (cm)")
    ax.set_xlabel("Testgruppe")
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(beschriftung)

    plt.show()  # Graphik darstellen


def beispiele():
    """Beispiel Matplotlib C - Hauptprogramm"""
    graphik_1()
    graphik_2()
    graphik_3()
    graphik_4()
    graphik_5()
    graphik_6()


beispiele()
