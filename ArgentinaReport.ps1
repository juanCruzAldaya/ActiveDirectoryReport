﻿if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
    # Get the current script path
    $scriptPath = $myinvocation.mycommand.definition

    # Start a new PowerShell process with elevated privileges
    Start-Process powershell -Verb runAs -ArgumentList "& '$scriptPath'"
    Break  # Exit the current script
}


$users = Get-ADUser -Filter 'a-countryDescription -eq "Argentina"'  -Properties OfficePhone, a-personnelNumber -SearchBase "OU=People,DC=dir,DC=svc,DC=accenture,DC=com"

$users | Export-Csv -Path "C:\ADReport\UsersArgentina.csv" -NoTypeInformation
