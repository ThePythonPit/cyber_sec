import os
from datetime import datetime
import subprocess
from urllib.parse import urlparse
import dotenv

# Carica le variabili d'ambiente dal file .env
dotenv.load_dotenv()

# Ottiene l'URI del database e il percorso di backup dalle variabili d'ambiente
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
BACKUP_PATH = os.getenv('BACKUP_PATH')

# Estrae i componenti dall'URI del database
parsed_uri = urlparse(SQLALCHEMY_DATABASE_URI)
dbname = parsed_uri.path[1:]  # Rimuove lo slash iniziale
user = parsed_uri.username
password = parsed_uri.password
host = parsed_uri.hostname
port = parsed_uri.port

# Genera il nome del file di backup con timestamp
file_name = f"{dbname}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
backup_file_path = os.path.join(BACKUP_PATH, file_name)

# Comando per il backup
backup_cmd = f"mysqldump -h {host} -P {port} -u {user} --password={password} {dbname} > {backup_file_path}"

# Esegue il comando (assicurati che il percorso di mysqldump sia nel PATH o specifica il percorso completo)
print("Eseguendo il backup del database...")
result = subprocess.run(backup_cmd, shell=True, check=True)

if result.returncode == 0:
    print(f"Backup completato: {backup_file_path}")
else:
    print("Si è verificato un errore durante il backup del database.")
