/*
    Das SQL-Skript erzeugt eine neue Beispieldatenbank.
	In dieser wird eine Tabelle mit einigen Einträgen angelegt.
 
    Einordnung:			FISI-LF5-LS3-Beispiel-01
    Aufgabe: 			beispiel_ls3_01.sql

    Name:				Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			14.03.2019
    Letzte Änderung:	11.05.2021

*/

DROP DATABASE IF EXISTS beispiel_ls3_01;                       # Evtl. vorhandene Datenbank löschen

CREATE DATABASE beispiel_ls3_01 default character set utf8;    # Neue Beispieldatenbank anlegen

USE beispiel_ls3_01;                                           # Mit neuer Datenbank verbinden

CREATE TABLE cpu_log (                                         # Neue Tabelle in Beispieldatenbank anlegen
	t1_ID	int(11) NOT NULL AUTO_INCREMENT,
    t1_zeit	DATETIME DEFAULT NOW(),
    t1_wert	DECIMAL(9,2),
    PRIMARY KEY (t1_ID)
    );
