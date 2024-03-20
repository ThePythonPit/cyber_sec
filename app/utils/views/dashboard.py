from flask import Blueprint, render_template
from flask_socketio import SocketIO, emit

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates')

@dashboard_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Inizializza SocketIO nel file `app/__init__.py` e utilizzalo qui per inviare dati in tempo reale al frontend.
