from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
jwt = JWTManager()
login_manager = LoginManager()
mail = Mail()



# Configura qui le impostazioni specifiche delle estensioni, come i callback di login_manager
@login_manager.user_loader
def load_user(user_id):
    from ..models import User  # Import qui per evitare import circolari
    return User.query.get(int(user_id))
