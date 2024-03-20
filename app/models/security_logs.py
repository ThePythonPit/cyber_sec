from app.utils.extensions import db

class SecurityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    level = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    user = db.Column(db.String(100), nullable=True)
    ip = db.Column(db.String(100), nullable=True)

  