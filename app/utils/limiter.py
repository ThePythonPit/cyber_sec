"""from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def init_limiter(app):
    limiter = Limiter(
        key_func=get_remote_address,  # Utilizza l'indirizzo IP del client come chiave
        app=app,
        default_limits=["200 per day", "50 per hour"]  # Limiti di default per ogni utente
    )
    return limiter"""

