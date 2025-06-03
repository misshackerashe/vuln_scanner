import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scanner.core import start_scan
import customtkinter as ctk
from scanner.core import start_scan
import json
import datetime
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🛡️ VulnScanner Pro")
        self.geometry("750x600")
        self.configure(padx=20, pady=20)

        # Título principal
        self.title_label = ctk.CTkLabel(self, text="Vulnerability Scanner", font=ctk.CTkFont("Courier", 26, "bold"))
        self.title_label.pack(pady=10)

        # Input para IP o dominio
        self.target_entry = ctk.CTkEntry(self, placeholder_text="Enter target IP or hostname", width=450)
        self.target_entry.pack(pady=10)

        # Menú desplegable de protocolo
        self.protocol_option = ctk.CTkOptionMenu(self, values=["TCP", "UDP"])
        self.protocol_option.pack(pady=5)

        # Modo de escaneo
        self.scan_mode = ctk.CTkOptionMenu(self, values=["Stealth", "Aggressive"])
        self.scan_mode.pack(pady=5)

        # Botón de escaneo
        self.scan_button = ctk.CTkButton(self, text="Start Scan 🔎", command=self.start_scan_thread)
        self.scan_button.pack(pady=15)

        # Barra de progreso
        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=5)

        # Caja de resultados
        self.result_box = ctk.CTkTextbox(self, width=700, height=300, font=("Courier", 12))
        self.result_box.pack(pady=15)

    def start_scan_thread(self):
        threading.Thread(target=self.run_scan).start()

    def run_scan(self):
        target = self.target_entry.get()
        protocol = self.protocol_option.get()
        mode = self.scan_mode.get()

        if not target:
            self.result_box.insert("end", "[!] Please enter a valid target.\n")
            return

        self.result_box.delete("1.0", "end")
        self.result_box.insert("end", f"[+] Target: {target}\n")
        self.result_box.insert("end", f"[+] Protocol: {protocol} | Mode: {mode}\n\n")

        self.progress_bar.set(0.2)
        results = start_scan(target, protocol=protocol.lower(), mode=mode.lower())
        self.progress_bar.set(0.7)

        if not results:
            self.result_box.insert("end", "[✓] No vulnerabilities found.\n")
        else:
            for res in results:
                self.result_box.insert("end", f"[!] Port {res['port']} - {res['vulnerability']}\n")

        self.result_box.insert("end", "\n[✓] Scan complete.\n")
        self.progress_bar.set(1.0)

        self.save_log(target, protocol, mode, results)

    def save_log(self, target, protocol, mode, results):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"scan_log_{timestamp}.json"
        log_data = {
            "timestamp": timestamp,
            "target": target,
            "protocol": protocol,
            "mode": mode,
            "results": results,
        }

        with open(filename, "w") as f:
            json.dump(log_data, f, indent=4)

        self.result_box.insert("end", f"\n[📝] Log saved as {filename}\n")


if __name__ == "__main__":
    app = ScannerApp()
    app.mainloop()
