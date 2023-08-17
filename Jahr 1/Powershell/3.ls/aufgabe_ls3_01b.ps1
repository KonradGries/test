param ([int] $zahl1,[int] $zahl2,[switch] $add,[switch] $sub,[switch] $mul, [switch] $div)

[float] $Summe = 0
if ($add -eq $true) {
    $summe = $zahl1 + $zahl2 
    write-host "Das Ergebniss ist $summe"
    }
    elseif ($sub -eq $true) {
        $summe = $zahl1 - $zahl2
        write-host "Das Ergebniss ist $summe"
    }
    elseif ($mul -eq $true){
        $summe = $zahl1 * $zahl2
        write-host "Das Ergebniss ist $summe" 
    }
    elseif ($div -eq $true){
        $summe = $zahl1 / $zahl2
        write-host "Das Ergebniss ist $summe"
    }
    