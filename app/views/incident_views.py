# app/views/incident_views.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
# Usa importazioni relative qui
from ..forms.security_incident_form import SecurityIncidentForm
from app.models.securityincident import SecurityIncident
from app.utils.extensions import db

# Creazione di un Blueprint per le viste degli incidenti
incident_bp = Blueprint('incident_bp', __name__, template_folder='templates')

@incident_bp.route('/report-incident', methods=['GET', 'POST'])
def report_incident():
    form = SecurityIncidentForm()
    if form.validate_on_submit():
        # Creazione di una nuova istanza di SecurityIncident
        # con i dati raccolti dal form
        incident = SecurityIncident(
            title=form.title.data,
            description=form.description.data,
            # Assicurati di aggiungere altri campi come necessario
        )
        db.session.add(incident)
        db.session.commit()
        flash('Incidente segnalato con successo.', 'success')
        return redirect(url_for('incident_bp.index'))  # Assicurati che 'index' sia la vista corretta
    return render_template('report_incident.html', form=form)

# Assicurati di avere una vista 'index' o modifica la redirect qui sopra
# con una destinazione appropriata.
@incident_bp.route('/')
def index():
    return render_template('index.html')
