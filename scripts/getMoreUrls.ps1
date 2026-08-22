param(
    [Parameter(Mandatory = $true)]
    [string]$Target
)

$Waymore = "waymore"
$OutputDir = ".\$Target"

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

Write-Host "[*] Executando Waymore para $Target..."

& $Waymore `
    -i $Target `
    -mode U `
    -oU "$OutputDir\urls.txt"

Write-Host ""
Write-Host "[+] Finalizado!"
Write-Host "[+] URLs      : $OutputDir\urls.txt"
