clear-host
write-host "Rechner"
Write-host "_______________" 
Write-host ""

[float] $zahl1 = read-host "Gibt eine Zahl ein" 
[float] $zahl2 = read-host "Gibt noch eine Zahl ein"
write-host ""

$addition = $zahl1 + $zahl2
$subtraktion  = $zahl1 - $zahl2
$Produkt  = $zahl1 * $zahl2
write-host "Addition: $addition"
write-host "Subtraktion: $subtraktion"
write-host "Produkt: $Produkt"