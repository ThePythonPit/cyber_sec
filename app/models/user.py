from datetime import datetime, timedelta
from flask import current_app
from itsdangerous import URLSafeTimedSerializer as Serializer
from app.utils.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .permission import Permission

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # La relazione 'users' è definita nella classe User con backref
    permissions = db.relationship('Permission', secondary='role_permissions', backref=db.backref('roles'))

# Tabella di associazione per la relazione many-to-many tra Role e Permission
role_permissions = db.Table('role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    login_attempts = db.Column(db.Integer, default=0)
    lock_until = db.Column(db.DateTime)
    role = db.relationship('Role', backref='users')
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expires_in=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    def verify_confirmation_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=3600)  # Aggiunto max_age per specificare la durata del token
        except:
            return False
        if data.get('user_id') != self.id:
            return False
        self.confirmed = True
        db.session.commit()
        return True

    def is_account_locked(self):
        if self.lock_until is None:
            return False
        return datetime.now() < self.lock_until

    def lock_account(self, minutes=30):
        self.lock_until = datetime.now() + timedelta(minutes=minutes)
        db.session.commit()

    def reset_login_attempts(self):
        self.login_attempts = 0
        db.session.commit()

    def increment_login_attempts(self):
        self.login_attempts += 1
        db.session.commit()

    def can(self, permission_name):
        permission = Permission.query.filter_by(name=permission_name).first()
        if not permission or not self.role:
            return False
        return permission in self.role.permissions

    def __repr__(self):
        return f'<User {self.username}>'
hashed_password = generate_password_hash('123456')
print(len(hashed_password), hashed_password)

(Role)