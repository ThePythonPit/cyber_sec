# tests/test_logs.py
import pytest
from flask import url_for
from app import create_app
from app.models import SecurityLog
from app.utils.extensions import db

@pytest.fixture
def app():
    """Crea e configura una nuova app per ogni test."""
    app = create_app('testing')  # Assumi di avere una configurazione di testing che disabilita CSRF e usa un DB di test
    with app.app_context():
        db.create_all()  # Crea le tabelle per il test
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Un client di test per l'app."""
    return app.test_client()

def test_get_logs_no_filter(client):
    """Test senza filtri."""
    # Creazione di un log di test nel database
    log = SecurityLog(timestamp='2021-01-01 12:00:00', level='INFO', message='Test message', user='testuser', ip='127.0.0.1')
    db.session.add(log)
    db.session.commit()

    response = client.get(url_for('logs_bp.get_logs'))
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['user'] == 'testuser'

def test_get_logs_with_user_filter(client):
    """Test con filtro utente."""
    # Aggiunta di un log di test
    log1 = SecurityLog(timestamp='2021-01-01 12:00:00', level='INFO', message='User test', user='user1', ip='127.0.0.1')
    log2 = SecurityLog(timestamp='2021-01-02 13:00:00', level='WARNING', message='Another user test', user='user2', ip='127.0.0.2')
    db.session.add_all([log1, log2])
    db.session.commit()

    response = client.get(url_for('logs_bp.get_logs') + '?user=user1')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['user'] == 'user1'
    assert data[0]['message'] == 'User test'
 
