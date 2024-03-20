from flask_mail import Mail, Message
from flask import current_app, render_template

mail = Mail()

def init_app(app):
    mail.init_app(app)

def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[to], sender=app.config['MAIL_DEFAULT_SENDER'])
    msg.body = render_template(f"{template}.txt", **kwargs)
    msg.html = render_template(f"{template}.html", **kwargs)
    with app.app_context():
        mail.send(msg)
