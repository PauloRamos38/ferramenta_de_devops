"""
Flask API simples para demonstração de DevOps
"""
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para requisições do dashboard

# Configurar caminho para arquivos estáticos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = BASE_DIR

@app.route('/')
def index():
    """Servir o dashboard HTML"""
    return send_from_directory(STATIC_DIR, 'index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'flask-api',
        'version': '1.0.0'
    }), 200

@app.route('/api/users')
def get_users():
    """Endpoint de exemplo - lista de usuários"""
    users = [
        {'id': 1, 'name': 'Paulo', 'role': 'DevOps Engineer'},
        {'id': 2, 'name': 'Emma', 'role': 'Developer'},
        {'id': 3, 'name': 'Lucas', 'role': 'SRE'}
    ]
    return jsonify({
        'users': users,
        'total': len(users)
    })

@app.route('/api/info')
def get_info():
    """Informações sobre o projeto"""
    return jsonify({
        'project': 'Flask API with Docker & CI/CD',
        'author': 'Paulo Ramos',
        'github': 'https://github.com/PauloRamos38',
        'technologies': ['Flask', 'Docker', 'GitHub Actions', 'pytest'],
        'description': 'API REST demonstrando práticas DevOps'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
          
