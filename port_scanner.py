import socket
from datetime import datetime

def verificar_porta(ip, porta):
    # Cria um socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Define um tempo limite curto para a resposta não travar
    
    try:
        # Tenta se conectar ao IP e à porta informados
        resultado = s.connect_ex((ip, porta))
        if resultado == 0:
            return True # Porta ABERTA
        else:
            return False # Porta FECHADA
    except:
        return False
    finally:
        s.close()

def main():
    print("=" * 45)
    print("       VERIFICADOR DE PORTAS (PORT SCANNER)")
    print("=" * 45)
    
    # Pede o alvo ao usuário (pode ser um IP ou localhost)
    alvo = input("Digite o IP ou domínio para escanear (ex: 127.0.0.1 ou scanme.nmap.org): ").strip()
    
    # Dicionário de portas comuns e seus serviços para facilitar a leitura
    portas_comuns = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP (Web)",
        110: "POP3",
        443: "HTTPS (Web Segura)",
        3306: "MySQL",
        3389: "RDP (Área de Trabalho Remota)"
    }
    
    print(f"\nIniciando varredura no alvo: {alvo}")
    inicio_tempo = datetime.now()
    
    portas_abertas = 0
    print(f"\n{'PORTA':<8} | {'SERVIÇO':<20} | {'STATUS'}")
    print("-" * 42)
    
    for porta, servico in portas_comuns.items():
        if verificar_porta(alvo, porta):
            print(f"{porta:<8} | {servico:<20} | [ABERTA]")
            portas_abertas += 1
        else:
            print(f"{porta:<8} | {servico:<20} | [FECHADA]")
            
    fim_tempo = datetime.now()
    duracao = fim_tempo - inicio_tempo
    
    print("-" * 42)
    print(f"Varredura finalizada em {duracao.total_seconds():.2f} segundos.")
    print(f"Total de portas abertas encontradas: {portas_abertas}")
    
    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()