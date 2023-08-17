$Running = Get-Service | Where-Object {$_.Status -eq "running"} | measure 
write-host "Es gibt "$Running.count " laufende Prozesse"

$Running = Get-Service | Where-Object {$_.Status -eq "stopped"} | measure 
write-host "Es gibt "$Running.count " gestoppte Prozesse"

