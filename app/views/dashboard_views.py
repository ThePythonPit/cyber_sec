from flask import Blueprint, render_template
import plotly.express as px
import json

from flask import Blueprint, render_template
import plotly.express as px
import json

# Crea un nuovo blueprint per la dashboard
dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # Crea un semplice grafico con Plotly
    fig = px.line(x=["a", "b", "c"], y=[1, 3, 2], title="sample figure")
    
    # Converti il grafico in JSON
    graphJSON = json.dumps(fig, cls=px.utils.PlotlyJSONEncoder)
    
    # Passa il grafico al template
    return render_template('dashboard.html', graphJSON=graphJSON)
