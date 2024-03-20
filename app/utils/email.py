from flask_mail import Message
from ..utils.extensions import mail
from flask import current_app, render_template

def send_email(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to], sender=current_app.config['MAIL_DEFAULT_SENDER'])
    msg.body = render_template(f"{template}.txt", **kwargs)
    msg.html = render_template(f"{template}.html", **kwargs)
    try:
        mail.send(msg)
    except Exception as e:
        # Logga l'errore o gestiscilo come necessario
        print(f"Errore nell'invio dell'email: {e}")
