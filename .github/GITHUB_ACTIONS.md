# GitHub Actions CI/CD Pipeline

Este projeto possui um pipeline completo de CI/CD automatizado com GitHub Actions.

## 📋 Workflows Configurados

### 1. **CI/CD Pipeline** (`.github/workflows/ci.yml`)
Executado automaticamente em cada commit e pull request:

- **Test Job**: Executa testes com cobertura de código
- **Build Job**: Constrói a imagem Docker e testa
- **Lint Job**: Verifica qualidade de código com flake8
- **Deploy Job**: Cria summary de status e status annotation

**Trigger:**
- Push em `main` ou `develop`
- Pull requests para `main`
- Manual trigger (workflow_dispatch)

### 2. **Deploy to Docker Hub** (`.github/workflows/deploy.yml`)
Deploya a imagem Docker para Docker Registry:

- **Build & Push**: Constrói e envia imagem para Docker Hub
- **Security Scan**: Escaneia vulnerabilidades com Trivy
- **Tests**: Valida endpoints da API antes de enviar

**Trigger:**
- Push em `main` com mudanças em `app/`, `Dockerfile` ou `docker-compose.yml`
- Manual trigger (workflow_dispatch)

## 🔧 Configuração

### Secrets Necessários para Deploy

Para fazer o push da imagem Docker para Docker Hub, configure estes secretos no GitHub:

1. Acesse: `Settings → Secrets and variables → Actions`
2. Crie novo secret:
   - **DOCKER_USERNAME**: Seu username no Docker Hub
   - **DOCKER_PASSWORD**: Seu token/senha do Docker Hub

Exemplo:
```bash
# No seu repositório GitHub
Settings → Secrets and variables → Actions → New repository secret
  Name: DOCKER_USERNAME
  Value: seu_usuario_docker_hub

  Name: DOCKER_PASSWORD  
  Value: seu_token_docker_hub
```

## 📊 Status de Execução

Você pode acompanhar os workflows em:

`GitHub → Actions`

Cada workflow mostra:
- ✅ Status de cada job
- ⏱️ Tempo de execução
- 📝 Logs detalhados
- 📦 Artifacts gerados

## 🚀 Como Usar

### Executar Pipeline Manualmente

1. Vá para `GitHub Actions`
2. Selecione o workflow desejado
3. Clique em `Run workflow`
4. Selecione a branch
5. Clique em `Run workflow`

### Verificar Resultados

```bash
# Ver status dos últimos workflows
gh run list --repo PauloRamos38/ferramenta_de_devops

# Ver detalhes de um workflow específico
gh run view <run-id> --repo PauloRamos38/ferramenta_de_devops

# Ver logs de um job
gh run view <run-id> --job <job-id> --log
```

## 📈 Métricas de Sucesso

Cada pipeline reporta:

- ✅ **Tests**: Número de testes passando
- 📊 **Coverage**: % de cobertura de código
- 🐳 **Docker Build**: Imagem construída com sucesso
- 🔍 **Linting**: Verificação de qualidade de código
- 🔒 **Security**: Vulnerabilidades encontradas (se houver)

## 🔄 Histórico de Execuções

Todos os workflows executados podem ser acessados em:

```
GitHub → Actions → [Workflow Name]
```

Cada execução mostra:
- Que commit triggerou
- Quem iniciou (se manual)
- Resultado (sucesso/falha)
- Tempo de execução
- Logs completos de cada job

## 📝 Logs e Debugging

Para troubleshoot de problemas:

1. Acesse `GitHub Actions`
2. Clique no workflow com problemas
3. Clique no job falhado
4. Expanda os passos para ver logs
5. Procure por erros (🔴 linhas em vermelho)

Erros comuns:
- `Connection refused`: Aplicação não iniciou
- `Module not found`: Dependência não instalada
- `Unauthorized`: Secrets não configurados

## 🎯 Próximos Passos

1. ✅ Configure DOCKER_USERNAME e DOCKER_PASSWORD
2. ✅ Faça um push para triggar o pipeline
3. ✅ Monitore em `GitHub → Actions`
4. ✅ Verifique imagens em `Docker Hub` (se configurado)

## 📞 Suporte

Para mais informações sobre GitHub Actions:
- [Documentação oficial](https://docs.github.com/en/actions)
- [Marketplace de Actions](https://github.com/marketplace?type=actions)
- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
