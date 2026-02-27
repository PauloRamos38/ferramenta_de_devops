# 🎨 Dashboard DevOps - Guia de Uso

## 📋 O que foi criado?

Uma apresentação moderna e interativa do seu projeto DevOps em um **dashboard HTML/CSS/JavaScript** que se conecta diretamente à sua API Flask.

## 🚀 Como Rodar

### Opção 1: Rodar Localmente (Recomendado)

```bash
# 1. Instale as dependências
pip install -r app/requirements.txt

# 2. Execute a aplicação Flask
python -m flask --app app.main run

# 3. Abra no navegador
# http://localhost:5000
```

### Opção 2: Com Docker Compose

```bash
# 1. Build e execute
docker-compose up --build

# 2. Abra no navegador
# http://localhost:5000
```

## 🎯 Features do Dashboard

✅ **Status em Tempo Real** - Verifica a saúde da API automaticamente
✅ **Design Responsivo** - Funciona em desktop, tablet e mobile
✅ **Métricas Visuais** - Exibe performance, cobertura de testes, latência
✅ **Integração API** - Carrega dados diretamente dos endpoints Flask
✅ **Auto-refresh** - Atualiza status a cada 30 segundos
✅ **Animações Suaves** - Interface moderna com transições CSS

## 🎨 Paleta de Cores

- **Primária**: Roxo/Azul vibrante (`#6366f1`)
- **Fundo**: Escuro minimalista (`#0f172a`)
- **Destaques**: Rosa neon (`#ec4899`)

## 📊 Seções do Dashboard

| Seção | Função |
|-------|--------|
| **Hero Card** | Apresentação principal do projeto |
| **Stats** | KPIs: Testes, Performance, Latência, Taxa de Sucesso |
| **API Status** | Health checks dos endpoints |
| **Server Info** | Informações do projeto e versão |
| **Equipe** | Lista de usuários (carregada da API) |
| **Tech Stack** | Tecnologias utilizadas |
| **Quick Links** | Links para GitHub e principais endpoints |
| **Arquitetura** | Visão geral da infraestrutura |

## 🔧 Customizações Possíveis

### Alterar Cores
Edite as variáveis CSS no topo do `index.html`:
```css
:root {
    --primary: #6366f1;      /* Cor primária */
    --accent: #ec4899;       /* Cor de destaque */
    --success: #10b981;      /* Cor de sucesso */
}
```

### Adicionar Mais KPIs
Adicione novos cards no grid de 4 colunas:
```html
<div class="card">
    <div class="card-label">Sua Métrica</div>
    <div class="card-value">100</div>
    <div style="color: var(--success); font-size: 12px;">Status</div>
</div>
```

### Mudar a Logo/Ícone
Altere os emojis nos cards (e.g., 🚀, ⚙️, 💻, etc.)

## 📱 Responsividade

O dashboard se adapta automaticamente para:
- 📺 **Desktop** (1400px+): Layout em grid completo
- 💻 **Tablet** (768px+): 2 colunas
- 📱 **Mobile** (<768px): 1 coluna, otimizado para toque

## 🔌 Endpoints Utilizados

O dashboard faz requisições para:

| Endpoint | Uso |
|----------|-----|
| `/` | Carrega o próprio dashboard |
| `/health` | Verifica saúde do serviço |
| `/api/users` | Carrega lista de usuários |
| `/api/info` | Carrega informações do projeto |

## ⚡ Performance

- **Tamanho do HTML**: ~35KB (sem compressão)
- **Requisições**: 3 chamadas AJAX ao carregar
- **Atualização**: A cada 30-60 segundos
- **Compatibilidade**: ✅ Chrome, Firefox, Safari, Edge

## 🐛 Troubleshooting

### Dashboard não carrega dados
- ✅ Verifique se a API está rodando em `http://localhost:5000`
- ✅ Verifique se flask-cors está instalado
- ✅ Abra o console (F12) para ver erros

### CORS Error
```
Access to XMLHttpRequest blocked by CORS policy
```
Solução: O `flask-cors` deve estar instalado e importado. Verifique o `app/main.py`.

### Porta 5000 já em uso
```bash
# Use outra porta:
python -m flask --app app.main run --port 8080
```
Depois atualize no dashboard a URL: `const API_BASE = 'http://localhost:8080'`

## 📦 Próximos Passos (Opcional)

- [ ] Adicionar gráficos com Chart.js
- [ ] Integrar com Prometheus para métricas históricas
- [ ] Adicionar autenticação JWT
- [ ] Implementar dark/light mode toggle
- [ ] Adicionar logs em tempo real
- [ ] Conectar webhooks do GitHub

---

**Criado com ❤️ para seu projeto DevOps** 🚀
