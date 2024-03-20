from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import urlparse
from app import db  # Assumi che `db` sia inizializzato in `app/__init__.py` e disponibile per l'importazione
from app.models.user import User
from app.utils.email import send_email
from itsdangerous import URLSafeTimedSerializer as Serializer
from app.utils.permissions import permission_required

bp = Blueprint('main', __name__, template_folder='templates')

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.home')
        return redirect(next_page)
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_exists = User.query.filter((User.username == username) | (User.email == email)).first()
        if user_exists:
            flash('An account with this username or email already exists.')
            return redirect(url_for('main.register'))

        # Assumendo che User abbia un costruttore che accetti username, email e password_hash
        password_hash = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

        # Opzionale: inviare una email di conferma qui, se necessario

        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset Your Password', 'email/reset_password', user=user, token=token)  # Assicurati che il template esista
            flash('An email with instructions to reset your password has been sent to you.')
        else:
            flash('No account found with that email.')
        return redirect(url_for('main.login'))
    return render_template('reset_password_request.html')

@bp.route('/admin_dashboard')
@login_required
@permission_required('admin_access')
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')

@bp.route('/test')
def test():
    return "La route di test funziona!"