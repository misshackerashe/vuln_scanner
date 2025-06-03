#VulnScanner

Un escáner de vulnerabilidades básico hecho en Python. Incluye backend modular y una interfaz gráfica atractiva con estilo ciberseguridad. Perfecto como proyecto de aprendizaje o base para herramientas más avanzadas.

---

#Características

- Detección básica de vulnerabilidades por banners.
- Carga dinámica de una base de datos `vuln_db.json`.
- Interfaz gráfica visual hecha con `CustomTkinter`.
- Soporte para guardar resultados en `.json` o `.txt`.
- Logs automáticos de los escaneos.
- Estilo visual "cyber" con DarkMode.
- Estructura profesional y lista para expansión.

---

# Roadmap

- [x] Backend funcional con análisis por puertos.
- [x] Base de datos de vulnerabilidades local.
- [x] Frontend inicial en CustomTkinter.
- [x] Guardado de logs.
- [ ] Dropdown para elegir protocolo (TCP/UDP).
- [ ] Barra de progreso en tiempo real.
- [ ] Gráficos tipo radar o gauges.
- [ ] Modo "stealth/agresivo" tipo Nmap.
- [ ] Exportación avanzada de reportes.
- [ ] Plugin system para vulnerabilidades.

---

# Requisitos

- Python 3.9+
- Paquetes:
  - `customtkinter`
  - `darkdetect`
  - `colorama` *(opcional para consola)*

Instálalos con:

```bash
pip install -r requirements.txt
Estructura del Proyecto
pgsql
Copiar
Editar
vuln_scanner/
├── scanner/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── ui/
│   └── app.py
├── data/
│   └── vuln_db.json
├── logs/
│   └── results.json
├── .venv/
├── requirements.txt
└── README.md
Cómo ejecutar
🔹 Activa el entorno virtual
Windows PowerShell:

bash
Copiar
Editar
.venv\Scripts\Activate.ps1
Linux/macOS:

bash
Copiar
Editar
source .venv/bin/activate
Lanza la app
Desde la raíz del proyecto:

bash
Copiar
Editar
python ui/app.py

Licencia
MIT License — libre uso con atribución. Úsalo para aprender, mejorar o construir sobre él.

 Disclaimer
Esta herramienta es con fines educativos. No la utilices sin autorización explícita. Escanear redes ajenas es ilegal y no es ético.

css
Copiar
Editar

