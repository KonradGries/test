""" beispiel_ls2_01b.py - GUI-Taschenrechner - Version B
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.02.2021, 07.10.2022
    Version b - Objekt-Orientierte-Programmierung
              - Ausnahmebehandlung (Exception-Handling)
              - Grid-Layout
              - Themed Tkinter (TTK)
    """


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Taschenrechner:
    """Klasse Taschenrechner"""

    def __init__(self):
        """Konstruktor, in dem das Taschenrechnerfenster aufgebaut wird"""

        self.hauptrahmen_anlegen()
        self.fensterelemente_anlegen()
        self.elementabstaende_setzen()

        self.fenster.mainloop()

    def hauptrahmen_anlegen(self):
        """Fenster und Hauptrahmen anlegen"""

        self.fenster = tk.Tk(className="Beispiel_ls2_01b")
        self.fenster.iconbitmap("bkgut.ico")

        self.hauptrahmen = ttk.Frame(master=self.fenster, padding="20")
        self.hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)

    def fensterelemente_anlegen(self):
        """Fensterelemente einfügen"""
        self.lbl_zahl_1 = ttk.Label(master=self.hauptrahmen, text="Zahl1")
        self.lbl_zahl_1.grid(column=1, row=1, columnspan=2, sticky="NW")

        self.wert_1 = tk.StringVar()
        self.zahl_1 = ttk.Entry(master=self.hauptrahmen, textvariable=self.wert_1)
        self.zahl_1.grid(column=3, row=1, columnspan=2, sticky="NWE")

        self.lbl_zahl_2 = ttk.Label(master=self.hauptrahmen, text="Zahl2")
        self.lbl_zahl_2.grid(column=5, row=1, columnspan=2, sticky="NW")

        self.wert_2 = tk.StringVar()
        self.zahl_2 = ttk.Entry(master=self.hauptrahmen, textvariable=self.wert_2)
        self.zahl_2.grid(column=7, row=1, columnspan=2, sticky="NWE")

        self.btn_add = ttk.Button(master=self.hauptrahmen, text="+", command=lambda: self.ausfuehren("+"))
        self.btn_add.grid(column=1, row=2, sticky="NW")

        self.btn_sub = ttk.Button(master=self.hauptrahmen, text="-", command=lambda: self.ausfuehren("-"))
        self.btn_sub.grid(column=2, row=2, sticky="NW")

        self.btn_mul = ttk.Button(master=self.hauptrahmen, text="x", command=lambda: self.ausfuehren("*"))
        self.btn_mul.grid(column=3, row=2, sticky="NW")

        self.btn_div = ttk.Button(master=self.hauptrahmen, text="/", command=lambda: self.ausfuehren("/"))
        self.btn_div.grid(column=4, row=2, sticky="NW")

        self.lbl_ergebnis = ttk.Label(master=self.hauptrahmen, text="Ergebnis")
        self.lbl_ergebnis.grid(column=1, row=3, columnspan=2, sticky="NW")

        self.wert_ergebnis = tk.StringVar()
        self.ergebnis = ttk.Entry(master=self.hauptrahmen, textvariable=self.wert_ergebnis)
        self.ergebnis.grid(column=3, row=3, columnspan=2, sticky="NWE")

    def elementabstaende_setzen(self):
        """Abstände setzen"""
        for element in self.hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")

    def ausfuehren(self, rechenart):
        """Allgemeine Rechenmethode mit Exception-Handling"""

        try:
            z_1 = float(self.wert_1.get())
            z_2 = float(self.wert_2.get())
            if rechenart == "+":
                erg = z_1 + z_2
            if rechenart == "-":
                erg = z_1 - z_2
            if rechenart == "*":
                erg = z_1 * z_2
            if rechenart == "/":
                erg = z_1 / z_2
        except ValueError:
            messagebox.showerror("Fehlermeldung", "Sie müssen eine Zahl eingeben!")
            self.wert_ergebnis.set("")
            return
        except ZeroDivisionError:
            messagebox.showerror("Fehlermeldung", "Sie dürfen nicht durch Null teilen!")
            self.wert_ergebnis.set("")
            return
        self.wert_ergebnis.set(str(erg))


Taschenrechner()
