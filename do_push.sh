#!/bin/bash
cd "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\ferramenta_de_devops"
git add .
git commit -m "Melhorar GitHub Actions CI/CD: adicionar deploy workflow e documentacao"
git push origin main
echo "Push completed!"
