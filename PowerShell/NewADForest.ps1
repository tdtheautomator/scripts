$domain_name = 'mycorp.org'
$ad_safe_pass = ConvertTo-SecureString 'P@ssword.123' -AsPlainText -Force

Start-Transcript -Path 'C:/NewADForest.log' -Force -Append

Write-Host "Configuring TCP/IP"
Get-NetAdapter | Where-Object Name -Like "Ethernet*"|Select-Object -First 1 | Rename-NetAdapter -Newname eth0 -PassThru
$nicIndex = (Get-NetAdapter -Name eth0).InterfaceIndex
#New-NetIPAddress -InterfaceIndex $nicIndex -IPAddress 10.10.14.50 -PrefixLength 24
Set-DnsClientServerAddress -InterfaceIndex $nicIndex -ServerAddresses ("10.10.14.50","10.10.14.60")

Write-Host "Installing Windows Features"
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

Write-Host "Importing ADDSDeployment Module"
Import-Module ADDSDeployment

Write-Host "Creating AD Forest"
Install-ADDSForest -DomainName $domain_name -SafeModeAdministratorPassword $ad_safe_pass `
-InstallDNS -Confirm:$False -NoRebootOnCompletion:$false -Force

Stop-Transcript
exit 0
