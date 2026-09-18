# 🔌 Python Port Scanner (Verificador de Portas)

Ferramenta leve desenvolvida em Python para escanear portas TCP comuns em um endereço IP ou domínio, identificando rapidamente quais serviços de rede estão ativos e abertos.

## 🚀 Tecnologias e Funcionalidades
* **Linguagem:** Python 3
* **Módulos Nativos:** `socket` (manipulação de conexões TCP de baixo nível) e `datetime` (medição de tempo de execução).
* **Principais Recursos:**
  * Varredura focada nas portas mais essenciais do dia a dia (FTP, SSH, HTTP, HTTPS, MySQL, RDP, etc.).
  * Tratamento de tempo limite (*timeout*) para evitar travamentos em portas filtradas ou fechadas.
  * Relatório formatado em tabela no terminal indicando o status detalhado ([ABERTA] / [FECHADA]).

## ⚙️ Como executar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `port_scanner.py`.
3. Execute no seu terminal:
   ```bash
   python port_scanner.py
4. Digite o IP ou domínio desejado (ex: 127.0.0.1) e acompanhe o diagnóstico das portas.
