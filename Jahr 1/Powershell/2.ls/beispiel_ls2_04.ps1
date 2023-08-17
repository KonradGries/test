 <#

.DESCRIPTION
        Beispielskript für eine Pipe

.NOTES

		Einordnung:			FISI-LF5-LS2-DIFF
		Projekt: 			beispiel_ls2_04
		Thema:				Beispielskript für eine Pipe

	Autor:
		Name:				Markus Breuer
		Organisaion:		BK-GuT

	Datum:
		Erstellt:			21.10.2020
		Letzte Änderung:	
#>

Clear-Host

Write-Host "Beispielskript für eine Pipe" -ForegroundColor Green
Write-Host "----------------------------`n" -ForegroundColor Green

Get-Process `
    | Sort-Object -Property cpu -Descending `
    | Where-Object {$_.Name -like "s*"} `
    | Select-Object cpu, id, name -first 10 `
    | Out-File -FilePath a.txt

Write-Host "Ergebnis in Datei a.txt geschrieben" -ForegroundColor Green