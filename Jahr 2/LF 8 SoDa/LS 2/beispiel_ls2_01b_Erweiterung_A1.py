""" Beispiel_ls2_01b mit Aufgabe 1d Erweiterung

    Demo-Beispiel, welches die GUI-Programmierung mit Python und Tkinter
    veranschaulicht.
    Es wird ein einfacher Taschenrechner realisiert mit Erweiterung von Aufgabe 1

    Einordnung:         FISI-LF8-LS2-Beispiele
    Aufgabe:            beispiel_ls2_01b

    Name:               Markus Breuer
    Organisaion:        BK-GuT

    Erstellt:           05.02.2021
    Letzte Änderung:    14.11.2021
    """

import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Taschenrechner:
    """ Klasse Taschenrechner """

    def __init__(self, hauptfenster):
        """ Konstruktor, in dem das Taschenrechnerfenster aufgebaut wird """
        self.fenster = hauptfenster
        self.fenster.iconbitmap("bkgut.ico")

        # Hauptrahmen anlegen
        self.hauptrahmen = ttk.Frame(master=self.fenster, padding="20")
        self.hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)

        # Fensterelemente einfügen
        self.lblZahl1 = ttk.Label(master=self.hauptrahmen, text="Zahl1")
        self.lblZahl1.grid(column=1, row=1, columnspan=2, sticky="NW")

        self.wert1 = StringVar()
        self.zahl1 = ttk.Entry(master=self.hauptrahmen, textvariable=self.wert1)
        self.zahl1.grid(column=3, row=1, columnspan=2, sticky="NWE")

        self.lblZahl2 = ttk.Label(master=self.hauptrahmen, text="Zahl2")
        self.lblZahl2.grid(column=5, row=1, columnspan=2, sticky="NW")

        self.wert2 = StringVar()
        self.zahl2 = ttk.Entry(master=self.hauptrahmen, textvariable=self.wert2)
        self.zahl2.grid(column=7, row=1, columnspan=2, sticky="NWE")

        self.btnAdd = ttk.Button(
            master=self.hauptrahmen, text="+", command=lambda: self.ausfuehren("+")
        )
        self.btnAdd.grid(column=1, row=2, sticky="NW")

        self.btnSub = ttk.Button(
            master=self.hauptrahmen, text="-", command=lambda: self.ausfuehren("-")
        )
        self.btnSub.grid(column=2, row=2, sticky="NW")

        self.btnMul = ttk.Button(
            master=self.hauptrahmen, text="x", command=lambda: self.ausfuehren("*")
        )
        self.btnMul.grid(column=3, row=2, sticky="NW")

        self.btnDiv = ttk.Button(
            master=self.hauptrahmen, text="/", command=lambda: self.ausfuehren("/")
        )
        self.btnDiv.grid(column=4, row=2, sticky="NW")

        self.lblErgebnis = ttk.Label(master=self.hauptrahmen, text="Ergebnis")
        self.lblErgebnis.grid(column=1, row=3, columnspan=2, sticky="NW")

        self.wert_ergebnis = StringVar()
        self.ergebnis = ttk.Entry(
            master=self.hauptrahmen, textvariable=self.wert_ergebnis
        )
        self.ergebnis.grid(column=3, row=3, columnspan=2, sticky="NWE")

        self.btnEnde = ttk.Button(
            master=self.hauptrahmen, text="Ende", command=lambda: self.beenden()
        )
        self.btnEnde.grid(column=7, row=3, columnspan=2, sticky="NWE")

        for element in self.hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")

    def ausfuehren(self, op):
        """ Allgemeine Rechenmethode mit Exception-Handling """
        try:
            z1 = float(self.wert1.get())
            z2 = float(self.wert2.get())
            if op == "+":
                erg = z1 + z2
            if op == "-":
                erg = z1 - z2
            if op == "*":
                erg = z1 * z2
            if op == "/":
                erg = z1 / z2
        except ValueError:
            messagebox.showerror("Fehlermeldung", "Sie müssen eine Zahl eingeben!")
            self.wert_ergebnis.set("")
            return
        except ZeroDivisionError:
            messagebox.showerror("Fehlermeldung", "Sie dürfen nicht durch Null teilen!")
            self.wert_ergebnis.set("")
            return
        self.wert_ergebnis.set(str(erg))

    def beenden(self):
        """ Programm beenden """
        sys.exit()

def hauptprogramm():
    fenster = Tk(className="Beispiel_ls2_01b")  # Rohes Fenster erstellen
    TS = Taschenrechner(fenster)  # Taschenrechneroberfläche aufbauen
    fenster.mainloop()  # Hauptschleife starten

hauptprogramm()