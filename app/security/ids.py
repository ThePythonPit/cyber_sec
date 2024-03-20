from flask import request, abort
import numpy as np
import logging

from sklearn.ensemble import IsolationForest

# Configura il logging
logging.basicConfig(level=logging.INFO)

class TrafficMonitor:
    def __init__(self, model):
        self.model = model

    def analyze(self, features):
        prediction = self.model.predict(np.array(features).reshape(1, -1))
        return prediction[0] == -1  # -1 indica un outlier/anomalia

def get_request_features(request):
    return [len(request.args), len(request.form)]

def detect_intrusion(model):
    # Lista bianca di percorsi che non richiedono il controllo IDS
    whitelist_paths = ['/', '/about', '/contact']
    if request.path in whitelist_paths:
        return  # Bypassa il rilevamento delle intrusioni per i percorsi nella lista bianca
    
    features = get_request_features(request)
    monitor = TrafficMonitor(model)
    if monitor.analyze(features):
        logging.warning(f"Sospetta attività di intrusione rilevata: {request.path}, features: {features}")
        abort(403, description="Attività sospetta rilevata")

def init_security_monitor(app, model):
    @app.before_request
    def before_request_func():
        detect_intrusion(model)

def detect_intrusion(model):
    whitelist_paths = ['/', '/about', '/contact', '/favicon.ico']
    if request.path in whitelist_paths:
        return


        """import json
from openai import OpenAI

try:
    with open("secrets.json") as f:
        secrets = json.load(f)
        api_key = secrets["api_key"]
except FileNotFoundError:
    print("Il file 'secrets.json' non è stato trovato.")
except KeyError:
    print("L'api_key non è stata trovata in 'secrets.json'.")

# Creiamo un oggetto client per autenticarci
client = OpenAI(api_key)

# Ora possiamo utilizzare l'API di ChatGPT per integrarlo nelle nostre applicazioni Python!
"""


