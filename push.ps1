&{
    Set-Location "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\ferramenta_de_devops"
    
    Write-Host "[1/3] Adding files..." -ForegroundColor Green
    & git add . 2>&1 | Write-Host
    
    Write-Host "[2/3] Committing..." -ForegroundColor Green
    & git commit -m "Melhorar GitHub Actions CI/CD: adicionar deploy workflow e documentacao" 2>&1 | Write-Host
    
    Write-Host "[3/3] Pushing..." -ForegroundColor Green
    & git push origin main 2>&1 | Write-Host
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ Push successful!" -ForegroundColor Green
    } else {
        Write-Host "`n⚠️ Push failed with code: $LASTEXITCODE" -ForegroundColor Yellow
    }
}
