from flask import Blueprint, render_template, current_app

admin_bp = Blueprint('admin_bp', __name__, template_folder='../templates')

@admin_bp.route('/dashboard')
def admin_dashboard():
    # Supponendo che 'current_app.storage.get_all()' recuperi i dati analizzati che vuoi mostrare
    dati_analizzati = current_app.storage.get_all()
    return render_template('admin_dashboard.html', dati_analizzati=dati_analizzati)
