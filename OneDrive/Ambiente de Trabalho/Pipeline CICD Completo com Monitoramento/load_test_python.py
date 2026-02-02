#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de teste de carga simulado - DevOps API
Simula requisições HTTP para testar performance
"""

import time
import requests
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import statistics

# Configuração
API_URL = "http://localhost:5000"
TIMEOUT = 5

class LoadTester:
    def __init__(self):
        self.results = []
        self.errors = []
        self.start_time = None
        self.end_time = None
    
    def test_health(self, num_requests=100, num_concurrent=10):
        """Teste de health check"""
        print("\n" + "="*60)
        print("1. TESTE DE HEALTH CHECK")
        print("="*60)
        print(f"Requisições: {num_requests} | Concorrentes: {num_concurrent}")
        
        self.start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=num_concurrent) as executor:
            futures = [executor.submit(self._make_request, f"{API_URL}/health") 
                      for _ in range(num_requests)]
            
            for i, future in enumerate(as_completed(futures)):
                try:
                    response_time, status_code = future.result()
                    self.results.append(response_time)
                    if (i + 1) % 20 == 0:
                        print(f"  Completadas {i + 1}/{num_requests} requisições...")
                except Exception as e:
                    self.errors.append(str(e))
        
        self._print_stats("Health Check")
    
    def test_create_task(self, num_requests=50, num_concurrent=5):
        """Teste de criação de tarefas"""
        print("\n" + "="*60)
        print("2. TESTE DE CRIAÇÃO DE TAREFAS")
        print("="*60)
        print(f"Requisições: {num_requests} | Concorrentes: {num_concurrent}")
        
        self.results = []
        self.start_time = time.time()
        
        task_data = {
            "title": "Test Task",
            "description": "This is a load test task"
        }
        
        with ThreadPoolExecutor(max_workers=num_concurrent) as executor:
            futures = [executor.submit(self._make_request, 
                                      f"{API_URL}/tasks", 
                                      method="POST", 
                                      json=task_data)
                      for _ in range(num_requests)]
            
            for i, future in enumerate(as_completed(futures)):
                try:
                    response_time, status_code = future.result()
                    self.results.append(response_time)
                    if (i + 1) % 10 == 0:
                        print(f"  Completadas {i + 1}/{num_requests} requisições...")
                except Exception as e:
                    self.errors.append(str(e))
        
        self._print_stats("Create Task")
    
    def test_get_tasks(self, num_requests=200, num_concurrent=20):
        """Teste de listagem de tarefas"""
        print("\n" + "="*60)
        print("3. TESTE DE LISTAGEM DE TAREFAS")
        print("="*60)
        print(f"Requisições: {num_requests} | Concorrentes: {num_concurrent}")
        
        self.results = []
        self.start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=num_concurrent) as executor:
            futures = [executor.submit(self._make_request, f"{API_URL}/tasks")
                      for _ in range(num_requests)]
            
            for i, future in enumerate(as_completed(futures)):
                try:
                    response_time, status_code = future.result()
                    self.results.append(response_time)
                    if (i + 1) % 40 == 0:
                        print(f"  Completadas {i + 1}/{num_requests} requisições...")
                except Exception as e:
                    self.errors.append(str(e))
        
        self._print_stats("Get Tasks")
    
    def _make_request(self, url, method="GET", json=None):
        """Faz uma requisição HTTP e retorna tempo de resposta"""
        try:
            start = time.time()
            if method == "GET":
                response = requests.get(url, timeout=TIMEOUT)
            elif method == "POST":
                response = requests.post(url, json=json, timeout=TIMEOUT)
            response_time = (time.time() - start) * 1000  # em ms
            return response_time, response.status_code
        except Exception as e:
            raise Exception(f"Erro na requisição: {str(e)}")
    
    def _print_stats(self, test_name):
        """Imprime estatísticas do teste"""
        if not self.results:
            print(f"❌ Nenhuma requisição bem-sucedida para {test_name}")
            return
        
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        
        min_time = min(self.results)
        max_time = max(self.results)
        avg_time = statistics.mean(self.results)
        median_time = statistics.median(self.results)
        
        if len(self.results) > 1:
            stdev = statistics.stdev(self.results)
        else:
            stdev = 0
        
        total_requests = len(self.results) + len(self.errors)
        success_rate = (len(self.results) / total_requests * 100) if total_requests > 0 else 0
        throughput = len(self.results) / duration if duration > 0 else 0
        
        print(f"\n📊 Resultados - {test_name}")
        print(f"  Tempo total: {duration:.2f}s")
        print(f"  Requisições bem-sucedidas: {len(self.results)}")
        print(f"  Erros: {len(self.errors)}")
        print(f"  Taxa de sucesso: {success_rate:.1f}%")
        print(f"\n⏱️  Tempos de resposta (ms):")
        print(f"  Mínimo: {min_time:.2f}ms")
        print(f"  Máximo: {max_time:.2f}ms")
        print(f"  Média: {avg_time:.2f}ms")
        print(f"  Mediana: {median_time:.2f}ms")
        print(f"  Desvio padrão: {stdev:.2f}ms")
        print(f"\n🚀 Throughput: {throughput:.2f} req/s")

def main():
    print("\n" + "="*60)
    print("🚀 TESTE DE CARGA - DevOps API")
    print("="*60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"API URL: {API_URL}")
    
    # Verificar conectividade
    try:
        response = requests.get(f"{API_URL}/health", timeout=TIMEOUT)
        if response.status_code == 200:
            print("✅ Aplicação está acessível")
        else:
            print(f"⚠️  API retornou status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Erro: Não foi possível conectar à API em {API_URL}")
        print("Certifique-se de que a aplicação está rodando.")
        return
    except Exception as e:
        print(f"❌ Erro ao conectar: {str(e)}")
        return
    
    tester = LoadTester()
    
    try:
        # Executar testes
        tester.test_health(num_requests=100, num_concurrent=10)
        time.sleep(1)  # Pausa entre testes
        
        tester.test_create_task(num_requests=50, num_concurrent=5)
        time.sleep(1)
        
        tester.test_get_tasks(num_requests=200, num_concurrent=20)
        
        # Resumo final
        print("\n" + "="*60)
        print("✅ TESTES CONCLUÍDOS COM SUCESSO")
        print("="*60)
        print(f"Total de requisições: {len(tester.results) + len(tester.errors)}")
        print(f"Bem-sucedidas: {len(tester.results)}")
        print(f"Erros: {len(tester.errors)}")
        
        if tester.results:
            print(f"Tempo médio de resposta: {statistics.mean(tester.results):.2f}ms")
        
        print("\n📊 Recomendações:")
        print("  • Revisar logs de erro se houver falhas")
        print("  • Aumentar replicas se CPU > 80%")
        print("  • Configurar auto-scaling (HPA)")
        print("  • Implementar cache se necessário")
        print("\n" + "="*60 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Teste interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro durante os testes: {str(e)}")

if __name__ == "__main__":
    main()
