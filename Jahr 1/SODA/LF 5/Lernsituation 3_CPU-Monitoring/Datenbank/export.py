import mysql.connector
import dblib as lib
import csv
import pandas as pd

def csvaus ():
    result = lib.dbAbfrageAnweisung(connection, "SELECT * FROM cpu_log ")
    for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
        print(str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]))
    #df = pd.DataFrame(result)
