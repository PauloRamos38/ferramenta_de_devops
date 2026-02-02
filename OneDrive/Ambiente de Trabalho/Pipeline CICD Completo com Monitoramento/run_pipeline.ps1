# Script para executar o pipeline completo

$pythonExe = "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\Pipeline CICD Completo com Monitoramento\.venv\Scripts\python.exe"
$projectDir = "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\Pipeline CICD Completo com Monitoramento"

Set-Location $projectDir

Write-Host "=== INICIANDO PIPELINE ===" -ForegroundColor Green
Write-Host ""

# Executar aplicação
Write-Host "1. Executando aplicação..." -ForegroundColor Cyan
& $pythonExe "Main · PY" --port=5000 &
$appPid = $?
Start-Sleep -Seconds 3

# Executar testes
Write-Host ""
Write-Host "2. Executando testes..." -ForegroundColor Cyan
& $pythonExe -m pytest "Test main · PY" -v

# Parar aplicação
if ($appPid) {
    Write-Host ""
    Write-Host "3. Parando aplicação..." -ForegroundColor Cyan
}

Write-Host ""
Write-Host "=== PIPELINE COMPLETO ===" -ForegroundColor Green
