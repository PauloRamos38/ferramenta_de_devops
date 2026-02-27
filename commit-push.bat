@echo off
cd /d "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\ferramenta_de_devops"

echo Adicionando arquivos...
git add .

echo.
echo Commit das mudanças...
git commit -m "Melhorar GitHub Actions CI/CD: adicionar deploy workflow e documentacao"

echo.
echo Fazendo push...
git push origin main

echo.
echo Done!
pause
