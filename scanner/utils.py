import json

def load_vulnerabilities(filepath="scanner/vuln_db.json"):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"[!] Error cargando base de datos de vulnerabilidades: {e}")
        return []
