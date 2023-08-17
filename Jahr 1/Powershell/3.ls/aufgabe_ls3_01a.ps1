$anzahl = $args.Length
write-host "Es gibt $anzahl Ergebnisse"

[float]$summe = 0
for($i = 0;$i -lt $args.Length;$i++) {
    $summe = $summe + $args[$i];
}

Write-Host "Das Ergebnis ist $summe "
