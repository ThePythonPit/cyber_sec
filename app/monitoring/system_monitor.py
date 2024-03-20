from flask import Blueprint, jsonify
import psutil
import subprocess
import shlex

monitor_bp = Blueprint('monitor', __name__)

@monitor_bp.route('/monitor')
def monitor():
    # Rimuovo l'intervallo per evitare il blocco della funzione
    cpu_usage = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return jsonify(cpu_usage=cpu_usage, memory=memory, disk_usage=disk_usage)

@monitor_bp.route('/network/traffic')
def get_network_traffic():
    # Uso un comando più sicuro e controllo maggiormente l'esecuzione dei comandi
    # In questo esempio, uso `netstat -e` come esempio di comando reale. Sostituire con il comando appropriato.
    command = "netstat -e"
    try:
        # Uso shlex.split per garantire che il comando sia diviso in modo sicuro per subprocess
        args = shlex.split(command)
        traffic_data = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return jsonify(traffic_data=traffic_data.decode('utf-8').strip())
    except subprocess.CalledProcessError as e:
        # Restituisco un messaggio di errore più dettagliato, includendo l'output del comando
        return jsonify(error="Command execution failed", details=e.output.decode('utf-8').strip()), 500

@monitor_bp.route('/cpu/usage')
def get_cpu_usage():
    # Riuso la logica per l'uso della CPU dalla funzione monitor
    cpu_usage = psutil.cpu_percent(interval=None)
    return jsonify(cpu_usage=cpu_usage)

def is_safe_url(url):
    """Funzione stub per la verifica dell'URL sicuro, se necessario in futuro."""
    return True  # Implementare la logica di verifica dell'URL qui

