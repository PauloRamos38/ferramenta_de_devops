@echo off
REM Script para executar o pipeline completo

cd "C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\Pipeline CICD Completo com Monitoramento"

echo === INICIANDO PIPELINE ===
echo.

REM Executar aplicação em background
echo 1. Executando testes...
".\.venv\Scripts\python.exe" -m pytest "Test main · PY" -v

echo.
echo === PIPELINE COMPLETO ===
