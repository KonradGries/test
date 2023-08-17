clear-host
write-host "Begrüßungsprogramm"
Write-host "__________________" 
Write-host ""

write-host "Hallo Guten Tag Herr/Frau $env:UserName "
write-host "Heute ist der:"
get-date 
Write-Host ""
write-host "Deine Geräteinfos:"
write-host ""
$env:computername
$ip = (Test-Connection $env:computername -Count 1).IPV4Address.ipAddressToString
write-host "Deine IP lautet:"
$ip
write-host "Du nutzt folgende Windows und Bios Version"
write-Host ""
Get-ComputerInfo | Select Osname, Biosbiosversion 
Write-Host "Prozessor:"
Get-WmiObject win32_processor |select name
write-host "Festplatten:"
Get-WmiObject win32_diskdrive |select model,Size
$ram = wmic OS get FreePhysicalMemory
write-host "Ramauslastung:"
$ram
Get-WmiObject win32_PhysicalMemory | select caption,capacity
get-content E:\bkgut\Powershell\Info.txt
