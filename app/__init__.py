from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
# Assicurati che gli import di estensioni siano corretti
from app.utils.extensions import db, jwt, login_manager, mail # Aggiusta il percorso se necessario
from config import Config

# Importazione dei Blueprint
from app.views.incident_views import incident_bp
from app.views.main_views import main_bp  # Assumendo che tu abbia questo file
from app.views.admin_views import admin_bp  # Devi creare questo per le viste admin
from app.monitoring.system_monitor import monitor_bp  # Import corretto del blueprint di monitoraggio

# Importazione dei modelli
# Assicurati di importare tutti i tuoi modelli qui, necessari per le migrazioni di Flask-Migrate
from app.models.user import User
from app.models.security_logs import SecurityLog

# Middleware e servizi personalizzati
from app.middleware.traffic_control import TrafficAnalyzerMiddleware
from app.services.in_memory_storage import InMemoryStorage, SimpleLimiter

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inizializzazione delle estensioni con l'app Flask
    db.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate = Migrate(app, db)

    # Caricamento delle variabili d'ambiente
    load_dotenv()

    # Inizializzazione dei servizi custom
    storage = InMemoryStorage()
    app.storage = storage  # Rendilo disponibile in tutta l'applicazione attraverso `current_app`
    limiter = SimpleLimiter()
    app.wsgi_app = TrafficAnalyzerMiddleware(app.wsgi_app, limiter, storage)

    # Registrazione della funzione user_loader per Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrazione dei blueprint
    app.register_blueprint(main_bp)  # Rotte principali (es. home, login, register)
    app.register_blueprint(incident_bp, url_prefix='/incidents')  # Rotte specifiche per gli incidenti
    app.register_blueprint(admin_bp, url_prefix='/admin')  # Rotte di amministrazione
    app.register_blueprint(monitor_bp, url_prefix='/monitoring')  # Blueprint per il monitoraggio del sistema

    return app
