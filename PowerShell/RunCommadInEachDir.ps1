$original_path = Get-Location
$target_path = "./ref-codes"
$cmd_exec = "git pull"
$folders = Get-ChildItem -path $base_path -Directory
$folders | ForEach-Object { 
                            Write-Host processing $_.Name in $target_path -ForegroundColor Yellow
                            Set-Location $_.FullName ; 
                            Invoke-Expression $cmd_exec}
Set-Location $original_path