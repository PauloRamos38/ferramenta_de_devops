const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve os arquivos estáticos da pasta principal
// __dirname é o diretório onde o script está rodando (a raiz do projeto)
app.use(express.static(path.join(__dirname, '/')));

app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));