#!/usr/bin/env pwsh

# Script para commit e push das mudanças do GitHub Actions

$RepoPath = "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\ferramenta_de_devops"

Write-Host "🚀 GitHub Actions Deploy - Commit & Push" -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Green
Write-Host ""

# Mudança para o diretório
Set-Location $RepoPath
Write-Host "📁 Working directory: $RepoPath" -ForegroundColor Cyan

# Status atual
Write-Host ""
Write-Host "📊 Git Status:" -ForegroundColor Cyan
git status --short

# Adicionar arquivos
Write-Host ""
Write-Host "➕ Adicionando arquivos..." -ForegroundColor Yellow
git add . 2>&1 | Out-Null

# Verificar se há mudanças
$status = git status --porcelain
if ($status) {
    Write-Host "✅ Arquivos preparados para commit" -ForegroundColor Green
    Write-Host ""
    
    # Commit
    Write-Host "📝 Fazendo commit..." -ForegroundColor Yellow
    $CommitMessage = "Melhorar GitHub Actions CI/CD: adicionar deploy workflow e documentacao"
    git commit -m $CommitMessage 2>&1 | Select-String -Pattern "^"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Commit realizado com sucesso!" -ForegroundColor Green
        Write-Host "   Mensagem: $CommitMessage" -ForegroundColor Gray
        Write-Host ""
        
        # Push
        Write-Host "📤 Fazendo push para origin/main..." -ForegroundColor Yellow
        git push origin main 2>&1 | Select-String -Pattern "^"
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "✅ Push realizado com sucesso!" -ForegroundColor Green
            Write-Host ""
            Write-Host "📊 GitHub Actions foi ativado!" -ForegroundColor Cyan
            Write-Host "   Acesse: https://github.com/PauloRamos38/ferramenta_de_devops/actions" -ForegroundColor Gray
            Write-Host ""
        } else {
            Write-Host "⚠️  Erro ao fazer push" -ForegroundColor Red
            Write-Host "   Verifique a conexão com o GitHub" -ForegroundColor Gray
        }
    } else {
        Write-Host "⚠️  Erro ao fazer commit" -ForegroundColor Red
    }
} else {
    Write-Host "ℹ️  Nenhuma mudança para commit" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=======================================" -ForegroundColor Green
Write-Host "✅ Processo concluído" -ForegroundColor Green
