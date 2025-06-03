import socket
import threading
from scanner.utils import load_vulnerabilities

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 8080]

vuln_db = load_vulnerabilities()

def match_vulnerability(banner):
    for entry in vuln_db:
        if entry["banner_signature"] in banner:
            return entry["vulnerability"]
    return None

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = s.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No banner"
            s.close()

            vuln = match_vulnerability(banner)
            if vuln:
                print(f"[!] Puerto {port} abierto | Banner: {banner}")
                print(f"    └─⚠️ VULNERABILIDAD DETECTADA: {vuln}")
            else:
                print(f"[+] Puerto {port} abierto | Banner: {banner}")
    except:
        pass

def start_scan(target, protocol="tcp", mode="stealth"):
    # Aquí va tu lógica de escaneo basada en protocolo y modo
    return [
        {"port": 80, "vulnerability": "Example Vuln 1"},
        {"port": 443, "vulnerability": "Example Vuln 2"},
    ]
    threads = []
    for port in COMMON_PORTS:
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
