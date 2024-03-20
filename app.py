"""
Imports Flask, render_template, SocketIO, and db from the flask and flask_socketio modules. Also imports login_manager and other extensions from app.utils.extensions.

Creates a Flask app, configures it, and initializes extensions like db and SocketIO. 

Sets up a simple route to render a template. 

Registers a SocketIO event handler to print messages from clients and send a response.

Exports the created app and SocketIO instance.
"""
from flask import Flask, render_template
from flask_socketio import SocketIO
# Assicurati di importare db dal file db.py correttamente, il percorso potrebbe variare a seconda della tua struttura
from app.utils.extensions import db, login_manager
# Importa i tuoi modelli qui, se sono definiti separatamente
# from app.models import User (ad esempio, se i tuoi modelli sono in app/models.py)

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cyber:cyber@localhost/cyber'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inizializza db con l'app Flask corrente
    db.init_app(app)
    socketio.init_app(app)
    
    # Importa i modelli qui, se necessario, o assicurati che siano importati altrove prima di fare operazioni sul db
    # Questo passaggio è necessario solo se utilizzi db.create_all() o funzioni simili

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('message_from_client')
    def handle_message(data):
        print('Received message: ', data)
        socketio.emit('message_from_server', {'data': 'This is a message from Flask.'})

    return app, socketio
