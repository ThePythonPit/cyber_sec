from flask import Flask, request
import time

app = Flask(__name__)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    total_time = time.time() - request.start_time
    app.logger.info(f"Richiesta a {request.path} completata in {total_time}s")
    return response
