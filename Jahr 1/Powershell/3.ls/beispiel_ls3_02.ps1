<#

.DESCRIPTION
        Beispielskript für den Aufruf eines Skripts.

.NOTES

	Inhalt:
		Einordnung:			FISI-DIFF-LS3
		Projekt: 			beispiel_ls3_02
		Thema:				1. Skriptaufruf aus PowerShell heraus
                            2. Dot Sourcing
                            3. Impliziete Skriptparameter ($args)

	Autor:
		Name:				Markus Breuer
		Organisaion:		BK-GuT

	Datum:
		Erstellt:			23.04.2019
		Letzte Änderung:	12.11.2020

#>

Write-Host "Hier ist das Skript beispiel_ls3_02"

$pi = 3.14                                              # Variable $pi anlegen

$anzahl = $args.Length                                  # Impliziete Parameterübergabe auswerten und anzeigen
Write-Host "Anzahl Parameter: $anzahl"
for( $i = 0; $i -lt $args.Length; $i++) {
    $parameter = $args[$i];
    Write-Host "Parameter $i : $parameter"
    }