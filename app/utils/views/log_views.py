from flask import Blueprint, request, jsonify
from app.utils.extensions import db
from ...models import SecurityLog
from sqlalchemy import or_

logs_bp = Blueprint('logs_bp', __name__)

@logs_bp.route('/logs', methods=['GET'])
def get_logs():
    # Recupera i filtri dai parametri della query, se presenti
    user = request.args.get('user')
    ip = request.args.get('ip')
    
    # Inizia la query
    query = SecurityLog.query
    
    # Applica filtri basati sui parametri della query, se forniti
    if user:
        query = query.filter(SecurityLog.user == user)
    if ip:
        query = query.filter(SecurityLog.ip == ip)
    
    # Esegui la query e recupera i risultati
    logs = query.order_by(SecurityLog.timestamp.desc()).all()

    # Converti i log in un formato JSON serializzabile
    logs_json = [{
        'timestamp': log.timestamp.isoformat(),
        'level': log.level,
        'message': log.message,
        'user': log.user,
        'ip': log.ip
    } for log in logs]
    
    # Ritorna i log come JSON
    return jsonify(logs_json)
