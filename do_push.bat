@echo off
setlocal enabledelayedexpansion

cd /d "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\ferramenta_de_devops"

echo [1/3] Adicionando arquivos...
git add .

echo [2/3] Fazendo commit...
git commit -m "Melhorar GitHub Actions CI/CD: adicionar deploy workflow e documentacao"

echo [3/3] Fazendo push...
git push origin main

echo.
echo Done!
