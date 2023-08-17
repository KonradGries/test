""" aufgabe_ls2_02.py - Anzeige des Primärenergiebedarfs mit Hilfe von TKinter
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  12.07.2021, 15.11.2022
    """


import tkinter as tk
import pandas as pd


class EnergieDaten:
    """Klasse EnergieDaten"""

    def __init__(self):
        """Konstruktor, in der die Daten aus der CSV-Datei eingelesen werden."""
        self.df = pd.read_csv("energiea.csv", sep=";")
        self.df.set_index("Energieträger", inplace=True)

    def energietraeger_holen(self):
        """Methode, um Liste der Energieträger bereitzustellen"""
        traeger_liste = list(self.df.index)
        return traeger_liste

    def kennwerte_holen(self, traeger):
        """Methode, um statistische Kennwerte für einen Energieträger bereitzustellen"""
        max_wert = self.df.loc[traeger].max()
        min_wert = self.df.loc[traeger].min()
        mittel_wert = round(self.df.loc[traeger].mean(), 2)
        return max_wert, min_wert, mittel_wert

    def jahreswerte_holen(self, traeger):
        """Methode, um Jahresverbräuche für einen Energieträger bereitzustellen"""
        jahres_liste = ["   Jahr  |  Verbrauch (PJ)"]
        jahre = list(self.df)
        for jahr in jahre:
            zeile = "  " + str(jahr) + "  |    " + str(self.df[jahr][traeger])
            jahres_liste = jahres_liste + [zeile]
        return jahres_liste


class EnergieGUI:
    """Klasse EnergieGUI"""

    def __init__(self):
        """Konstruktor, in dem das Hauptfenster aufgebaut wird"""
        print("Der Konstruktor baut das GUI auf")
        self.daten = EnergieDaten()
        self.fenster = tk.Tk(className="Aufgabe_ls2_02")
        self.fenster.mainloop()

    def beenden(self):
        """Beenden des Programms"""
        print("Diese Methode wird aufgerufen, wenn der Beenden Knopf gedrückt wird")

    def aktualisieren(self, event):
        """Aktualisieren von Tabelle (Liste) und Kennwerten"""
        print(
            "Diese Methode wird aufgerufen, wenn ein anderer Energieträger ausgewählt wird"
        )


def demo_hilfsmethoden():
    """zeigt, wie die Klasse Energiedaten genutzt werden kann; kann später wegfliegen"""
    daten = EnergieDaten()
    print("Liste der Energieträger")
    energie_traeger = daten.energietraeger_holen()
    print(energie_traeger)
    print("Kennwete des Energieträgers Gas")
    k_1, k_2, k_3 = daten.kennwerte_holen("Gase")
    print("k1: ", k_1, "  k2: ", k_2, "  k3: ", k_3)
    print("Jahres des Energieträgers Gas")
    jahresliste = daten.jahreswerte_holen("Gase")
    print(jahresliste)


def hauptprogramm():
    """Hauptprogramm"""
    EnergieGUI()
    demo_hilfsmethoden()


hauptprogramm()
