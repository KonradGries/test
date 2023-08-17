<#

.DESCRIPTION
        Beispielskript für ein Skript mit explizieten Parametern.

.NOTES

	Inhalt:
		Einordnung:			FISI-DIFF-LS3
		Projekt: 			beispiel_ls3_03
		Thema:				1. Expliziete Skriptparameter (param)

	Autor:
		Name:				Markus Breuer
		Organisaion:		BK-GuT

	Datum:
		Erstellt:			23.04.2019
		Letzte Änderung:	12.11.2020

#>

param( [string]$klasse, [int]$anzahl, [switch]$abschluss)

Write-Host "Hier ist das Skript beispiel_ls4_03"

Write-Host "Klasse: $klasse"
Write-Host "Anzahl: $anzahl"
Write-Host "Abschluss: $abschluss"

