""" beispiel_ls2_01a.py - GUI-Taschenrechner - Version A
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.02.2021, 06.07.2022
    """

from tkinter import *


def addieren():
    """ Funktion zum addieren """
    z1 = float(zahl1.get())
    z2 = float(zahl2.get())
    erg = z1 + z2
    setzeErgebnis(erg)


def subtrahieren():
    """ Funktion zum subtrahieren """
    z1 = float(zahl1.get())
    z2 = float(zahl2.get())
    erg = z1 - z2
    setzeErgebnis(erg)


def multiplizieren():
    """ Funktion zum multiplizieren """
    z1 = float(zahl1.get())
    z2 = float(zahl2.get())
    erg = z1 * z2
    setzeErgebnis(erg)


def dividieren():
    """ Funktion zum dividieren """
    z1 = float(zahl1.get())
    z2 = float(zahl2.get())
    erg = z1 / z2
    setzeErgebnis(erg)


def setzeErgebnis(erg):
    """ Funktion um Ergebnis auf Bildschirm auszugeben """
    ergebnis.delete(0, "end")
    ergebnis.insert(0, str(erg))


fenster = Tk(className="Beispiel_ls2_01a")  # Hauptfenster erstellen
fenster.iconbitmap("bkgut.ico")
fenster.geometry("400x200")

lblZahl1 = Label(master=fenster, text="Zahl1")  # Fensterelemente einfügen
lblZahl1.place(x=25, y=25, width=50, height=25)

zahl1 = Entry(
    master=fenster,
)
zahl1.place(x=100, y=25, width=75, height=25)

lblZahl2 = Label(master=fenster, text="Zahl2")
lblZahl2.place(x=200, y=25, width=50, height=25)

zahl2 = Entry(master=fenster)
zahl2.place(x=275, y=25, width=75, height=25)

btnAdd = Button(master=fenster, text="+", command=addieren)
btnAdd.place(x=25, y=75, width=25, height=25)

btnSub = Button(master=fenster, text="-", command=subtrahieren)
btnSub.place(x=75, y=75, width=25, height=25)

btnMul = Button(master=fenster, text="x", command=multiplizieren)
btnMul.place(x=125, y=75, width=25, height=25)

btnDiv = Button(master=fenster, text="/", command=dividieren)
btnDiv.place(x=175, y=75, width=25, height=25)

lblErgebnis = Label(master=fenster, text="Ergebnis")
lblErgebnis.place(x=25, y=125, width=50, height=25)

ergebnis = Entry(master=fenster)
ergebnis.place(x=100, y=125, width=75, height=25)

fenster.mainloop()  # Hauptschleife starten
