import csv
import requests

BASE_URL = "http://127.0.0.1:58001/api/v1"

# 1. Pedir credenciales por consola (evita dejar claves escritas en GitHub)
usuario = input("Usuario [cisco]: ").strip() or "cisco"
clave = input("Contraseña [class]: ").strip() or "class"

# 2. Obtener el serviceTicket (POST /ticket)
resp_ticket = requests.post(
    f"{BASE_URL}/ticket",
    json={"username": usuario, "password": clave},
    headers={"Content-Type": "application/json"},
)
resp_ticket.raise_for_status()
token = resp_ticket.json()["response"]["serviceTicket"]
headers = {"X-Auth-Token": token}

# 3. Consultar dispositivos de red y hosts (GET)
dispositivos = requests.get(f"{BASE_URL}/network-device", headers=headers).json()["response"]
hosts = requests.get(f"{BASE_URL}/host", headers=headers).json()["response"]

# 4. Exportar el inventario completo a CSV
with open("inventario_red.csv", mode="w", newline="", encoding="utf-8-sig") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Categoria", "Hostname", "IP", "Estado", "Detalle"])

    for dev in dispositivos:
        writer.writerow([
            "Dispositivo",
            dev.get("hostname", "N/A (ISP)"),
            dev.get("managementIpAddress", "N/A"),
            dev.get("collectionStatus", "N/A"),
            f"{dev.get('type', 'Equipo')} - IOS {dev.get('softwareVersion', 'N/A')}",
        ])

    for h in hosts:
        writer.writerow([
            "Host",
            h.get("hostName", "N/A"),
            h.get("hostIp", "N/A"),
            h.get("pingStatus", "N/A"),
            f"{h.get('hostType', 'Host')} en {h.get('connectedNetworkDeviceName', 'N/A')}",
        ])

print(f"Inventario exportado: {len(dispositivos)} dispositivos y {len(hosts)} hosts en 'inventario_red.csv'.")