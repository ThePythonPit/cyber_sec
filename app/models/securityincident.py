from app.utils.extensions import db, login_manager
from datetime import datetime
from .crud_mixin import CRUDMixin  


class SecurityIncident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='open')
    priority = db.Column(db.String(50), default='medium')  # Aggiunto campo "priorità"
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Aggiunto campo "assegnatario"
    
    # Relazione con il modello User (se esiste già)
    assignee = db.relationship('User', backref='assigned_incidents', foreign_keys=[assignee_id])

(SecurityIncident)
 