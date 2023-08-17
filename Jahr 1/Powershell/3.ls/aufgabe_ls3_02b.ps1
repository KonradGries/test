param ([switch]$add , [switch]$sub , [switch]$mul , [switch]$div , [float]$Z1 , [float]$Z2)

function add ([float]$Zahl1 , [float]$Zahl2) {
    $erg = $Zahl1 + $Zahl2
    return $erg
}

function sub ([float]$Zahl1 , [float]$Zahl2) {
    $erg = $Zahl1 - $Zahl2
    return $erg
}

function mul {
    param (
        [float]$Zahl1 , [float]$Zahl2
    )
    $erg = $Zahl1 * $Zahl2
    return $erg
}

function div {
    param (
        [float]$Zahl1 , [float]$Zahl2 
    )
    $erg = $Zahl1 / $Zahl2
    return $erg
}

if ($add -eq $true) {
    add $Z1 $Z2
}
elseif ($sub -eq $true) {
    sub $Z1 $Z2
}
elseif ($mul -eq $true) {
    mul $Z1 $Z2
}
elseif ($div -eq $true) {
    div $Z1 $Z2
}
else {
    Write-Host "Keine oder Falsche Parameter angegeben."
    exit
}