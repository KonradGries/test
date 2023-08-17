clear-host
write-host "Rechteckrechner"
Write-host "_______________" 
Write-host ""

[float] $laenge = read-host "Länge" 
[float] $breite = read-host "Breite"
write-host ""
$flaeche = $laenge * $breite
$umfang  = 2 * ($laenge + $breite)
write-host "Fläche: $flaeche"
write-host "Umfang: $umfang"
