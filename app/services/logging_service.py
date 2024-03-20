import logging
from logging.handlers import RotatingFileHandler
import os

def init_app(app, log_path='logs/myapp.log', level=logging.INFO):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(log_path, maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(level)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(level)
    app.logger.info('Logging setup completed')
