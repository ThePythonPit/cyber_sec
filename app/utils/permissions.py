from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def permission_required(permission):
    """
    Decoratore che verifica se l'utente corrente ha il permesso specificato.
    Se l'utente non ha il permesso, viene reindirizzato alla homepage con un messaggio flash.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                flash("Non hai il permesso necessario per accedere a questa pagina.", "warning")
                return redirect(url_for('main.home'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Qui aggiungiamo il nuovo decoratore admin_required
def admin_required(f):
    return permission_required('admin_access')(f)
