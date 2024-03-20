# app/forms/security_incident_form.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SecurityIncidentForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired()])
    description = TextAreaField('Descrizione', validators=[DataRequired()])
    submit = SubmitField('Segnala Incidente')
