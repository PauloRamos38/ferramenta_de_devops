#!/usr/bin/env python3
import subprocess
import os

os.chdir(r"C:\Users\User\Downloads\OneDrive\Ambiente de Trabalho\ferramenta_de_devops")

print("[1/3] Adicionando arquivos...")
subprocess.run(["git", "add", "."], check=False)

print("[2/3] Fazendo commit...")
result = subprocess.run(
    ["git", "commit", "-m", "Melhorar GitHub Actions CI/CD: adicionar deploy workflow e documentacao"],
    capture_output=True,
    text=True
)
print(result.stdout)
if result.stderr:
    print(result.stderr)

print("[3/3] Fazendo push...")
result = subprocess.run(
    ["git", "push", "origin", "main"],
    capture_output=True,
    text=True
)
print(result.stdout)
if result.stderr:
    print(result.stderr)

if result.returncode == 0:
    print("\n✅ Push realizado com sucesso!")
else:
    print(f"\n⚠️ Push retornou com código: {result.returncode}")
