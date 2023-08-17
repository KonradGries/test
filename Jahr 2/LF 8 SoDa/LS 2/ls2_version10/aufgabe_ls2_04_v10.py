"""Aufgabe_ls2_04 - Nutzungsdatensvisualisierung - Version1.0 - Ausgangsversion

    Einordnung:         FISI-LF8-LS2-A2 - keine Änderungen mehr - Zeilennummern !!!

    Name:               Markus Breuer
    Organisaion:        BK-GuT

    Erstellt:           10.12.2021
    Letzte Änderung:    26.12.2021
    """

import sys
import matplotlib
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import dblib

### Klasse NdsDaten ##########################################################

class NdsDaten:
    """ Klasse NdsDaten - Schnittstelle zur ndsdb-Datenbank """

    def __init__(self):
        """ Konstruktor, in der die Daten aus der CSV-Datei eingelesen werden. """
        self.host = ""
        self.user = ""
        self.passwd = ""
        self.db = ""
        self.tages_liste = None
        self.rechner_liste = None
        self.setze_db_verbindungsparameter()
        self.hole_rechner_daten()
        self.hole_anwendungs_daten()


    def setze_db_verbindungsparameter(self):
        """ Verbindungsparameter zur Datenbank liefern """
        self.host = "localhost"
        self.user = "root"
        self.passwd = ""
        self.db = "ndsdb"


    def hole_rechner_daten(self):
        """ Die Anzahl der Rechnernutzungen pro Tag werden aus der Datenbank geholt"""
        connection = dblib.dbVerbindungAufbauen(
            self.host, self.user, self.passwd, self.db
        )
        result = dblib.dbAbfrageAnweisung(
            connection, "SELECT datenTag, rdsOK FROM ndsimporte")
        self.tages_liste = []
        self.rechner_liste = []
        for zeile in result:  # Ergebnis zeilenweise durchlaufen und Listen füllen
            self.tages_liste = self.tages_liste + [zeile[0]]
            self.rechner_liste = self.rechner_liste + [zeile[1]]
        dblib.dbVerbindungAbbauen(connection)


    def hole_anwendungs_daten(self):
        """ Die Anzahl der Anwendungen pro Tag werden aus der Datenbank geholt """
        # Für V2.0 implementieren


    def hole_liste_rechner(self):
        """ Die Anzahl der Rechnernutzungen pro Tag in Form zweier Felder zurückgegeben """
        return self.tages_liste, self.rechner_liste


    def hole_liste_anwendungen(self):
        """ Die Anzahl derAnwendungsnutzungen pro Tag in Form zweier Felder zurückgegeben """
        # Für V2.0 implementieren


### Klasse NdsGui ############################################################

class NdsGui:
    """ Klasse NdsGui """

    def __init__(self):
        """ Konstruktor, in dem das Hauptfenster aufgebaut wird """

        self.daten = NdsDaten() # Zugriffsobjekt zur Datenbank erstellen
        self.fenster = Tk(className="Aufgabe_ls2_04 V1.0")  # Rohes Fenster erstellen

        self.festlegen_styles()  # Styles festlegen
        self.anlegen_hauptrahmen()  # Hauptrahmen anlegen und Gesamtfenster konfigurieren
        self.anlegen_fensterelemente()  # Fensterelemente einfügen
        self.feinschliff_layout()  # Abstände und Layout-Feinschliff

        self.fenster.mainloop()  # Hauptschleife starten


    def anlegen_hauptrahmen(self):
        """ Hauptrahmen anlegen und Gesamtfenster konfigurieren """
        self.fenster.iconbitmap("bkgut.ico")
        self.fenster.protocol("WM_DELETE_WINDOW", lambda: self.beenden())
        self.hauptrahmen = ttk.Frame(
            master=self.fenster, padding="20", style="Haupt.TFrame")
        self.hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)


    def anlegen_fensterelemente(self):
        """ Fensterelemente (Widgets) anlegen und positionieren """

        # Titel erstelen
        ttk.Label(master=self.hauptrahmen, text="Nutzungsdatenvisualisierung V1.0",
                  style="HauptLabel.TLabel").grid(column=1, row=1, columnspan=2, sticky="WE")

        # Bereich Rechnernutzung als Unterrahmen mit Inhalt erstellen
        self.unterrahmen1 = ttk.Frame(
            master=self.hauptrahmen, padding="10", style="Block.TFrame")
        self.unterrahmen1.grid(column=1, row=2, sticky="NWES")
        ttk.Label(master=self.unterrahmen1, text="Rechnernutzung", style="BlockLabel.TLabel").grid(
            column=1, row=1, columnspan=2, sticky="NW")
        self.rechner_liste = StringVar()
        self.liste1 = Listbox(master=self.unterrahmen1,
                              listvariable=self.rechner_liste)
        self.liste1.grid(column=1, row=2, sticky="NSWE")
        self.fuelle_rechner_liste()
        self.srollbar1 = ttk.Scrollbar(
            master=self.unterrahmen1, orient=VERTICAL, command=self.liste1.yview
        )
        self.srollbar1.grid(column=2, row=2, sticky="NSE")
        fig = Figure(figsize=(5, 4), dpi=100)
        tages_liste, rechner_liste = self.daten.hole_liste_rechner()
        fig.add_subplot().plot(tages_liste, rechner_liste)
        fig.autofmt_xdate(rotation=45)
        canvas = FigureCanvasTkAgg(fig, master=self.unterrahmen1)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=3, sticky="NW")

        # Bereich Anwendungsnutzung als Unterrahmen mit Inhalt erstellen
        self.unterrahmen2 = ttk.Frame(
            master=self.hauptrahmen, padding="5", style="Block.TFrame")
        self.unterrahmen2.grid(column=2, row=2, sticky="NWES")
        ttk.Label(master=self.unterrahmen2, text="Anwendungsnutzung",
            style="BlockLabel.TLabel").grid(column=1, row=1, columnspan=2, sticky="NW")
        ttk.Button(master=self.unterrahmen2, text="Anwendungsverteilung",
            command=lambda: self.anwendungsverteilung()).grid(column=1, row=4, columnspan=2, sticky="NE")
        # Für V2.0 Liste und Graphik implementieren
        ttk.Button(master=self.hauptrahmen, text="Beenden",
                   command=lambda: self.beenden()).grid(column=2, row=3, sticky="NE")


    def feinschliff_layout(self):
        """ Feinschliff Layout """

        # Elementabstände
        for element in self.hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")
        for element in self.unterrahmen1.winfo_children():
            element.grid_configure(padx="10", pady="10")
        self.liste1.grid_configure(padx="0", pady="10")
        self.srollbar1.grid_configure(padx="0", pady="10")

        # Verhalten bei Änderung der Fenstergröße
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)
        self.hauptrahmen.columnconfigure(1, weight=1)
        self.hauptrahmen.columnconfigure(2, weight=1)
        self.hauptrahmen.rowconfigure(1, weight=0)
        self.hauptrahmen.rowconfigure(2, weight=1)
        self.hauptrahmen.rowconfigure(3, weight=0)
        self.unterrahmen1.columnconfigure(1, weight=1)
        self.unterrahmen1.rowconfigure(1, weight=0)
        self.unterrahmen1.rowconfigure(2, weight=1)
        self.unterrahmen1.rowconfigure(3, weight=1)


    def festlegen_styles(self):
        """ Festlegen der genutzten Styles """

        HAUPT_BACKGROUND = "#b7d7e8"   # Hintergrundfarben
        BLOCK_BACKGROUND = "#cfe0e8"

        sblock = ttk.Style()

        sblock.configure('TLabel', font=("Tahoma", 11))
        sblock.configure('TButton', font=("Tahoma", 11))
        sblock.configure("Haupt.TFrame", background=HAUPT_BACKGROUND)
        sblock.configure(
            "HauptLabel.TLabel", background=HAUPT_BACKGROUND, font=("Tahoma", 24, "bold"))
        sblock.configure(
            "Block.TFrame", background=BLOCK_BACKGROUND, relief=RAISED)
        sblock.configure(
            "BlockLabel.TLabel", background=BLOCK_BACKGROUND, font=("Tahoma", 18, "bold"))


    def fuelle_rechner_liste(self):
        """ Die Methode fuelle_rechner_liste füllt die Liste mit Rechnernutzungen """
        tages_liste, rechner_liste = self.daten.hole_liste_rechner()
        liste = ["   Datum     |  Anzahl"]
        # Ergebnis zeilenweise durchlaufen und exportieren
        for tag, anzahl in zip(tages_liste, rechner_liste):
            zeilentext = tag.strftime("%d.%m.%Y") + \
                "  |    " + str(anzahl) + "\n"
            liste = liste + [zeilentext]
        self.rechner_liste.set(liste)


    def anwendungsverteilung(self):
        """ Methode zur Visualisierung der Anwendungsverteilung """
        # Für V2.0 implementieren


    def beenden(self):
        """ Beenden des Programms"""
        sys.exit()


### Startobjekt anlegen ##################################################

NdsGui()
