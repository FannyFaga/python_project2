import socket
import subprocess
import sys
from datetime import datetime
import threading


def detect_service(port):
    try:
        service = socket.getservbyport(port)
        return service
    except:
        return "Inconnu"

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        response = sock.connect_ex((ip, port))
        if response == 0:
            service = detect_service(port)
            print(f"Port {port}:    Ouvert ({service})")
        sock.close()
    except Exception as e:
        print(f"Erreur lors du scan du port {port}: {e}")


def main(): 
    subprocess.call("clear", shell=True)

    remoteServerIP = input("Entrez l'IP d'un serveur à scanner: ")
    start_port = int(input("Entrez le port de début (par défaut 1): ") or 1)
    end_port = int(input("Entrez le port de fin (par défaut 1024): ") or 1024)

    print("-" * 60)
    print(f"Lancement du scan des ports de la machine {remoteServerIP} (ports {start_port}-{end_port})")
    print("-" * 60)

    T1 = datetime.now()

 
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(remoteServerIP, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    T2 = datetime.now()
    D = T2 - T1
    print("-" * 60)
    print(f"Scan complété en : {str(D)}")
    print("-" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVous avez appuyé sur Ctrl+C. Arrêt du scan.")
        sys.exit()
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        sys.exit()