param ([switch]$fu1 , [switch]$fu2)

function f1 {
    Write-Host "Hier ist Funktion 1"
    [int]$N1 = 5
    [int]$N2 = 2
    f3 $N1
    f4 $N2
}

function f2 {
    Write-Host "Hier ist Funktion 2"
    [float]$N1 = 10
    [int]$N2 = 4
    f5 $N1 $N2
}

function f3 {
    param (
        [int]$NU1
    )
    Write-Host "Funktion 3"
    $erg = $NU1 - 4
    return $erg
}

function f4 {
    param (
        [int]$NU2
    )
    Write-Host "Funktion 4"
    $erg = 6 + $NU2
    return $erg
}

function f5 {
    param (
        [float]$NU1 , [float]$NU2
    )
    Write-Host "Funktion 5"
    $erg = $NU1 * $NU2
    return $erg
}

if ($fu1 -eq $true){
    f1
}
elseif ($fu2 -eq $true) {
    f2
}
else {
    Write-Host "Fehler bitte Paramenter angeben !"
}