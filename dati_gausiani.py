import numpy as np
import pandas as pd
from joblib import load
import plotly.express as px

# Percorso al file del modello salvato
model_path = 'C:\\Users\\J\\Desktop\\cybersec-prototype\\isolation_forest_model.joblib'

# Carica il modello salvato
model = load(model_path)

# Numero di esempi da generare
num_samples_normali = 20

# Generazione di dati con 12 caratteristiche, specificando un range ipotetico per ciascuna
# Nota: questi range sono esempi; dovresti adattarli in base alla conoscenza delle tue caratteristiche
ranges = [(-2, 2) for _ in range(12)]

# Generazione di dati normali basata sui range specifici
dati_normali = np.random.uniform(
    low=[r[0] for r in ranges],
    high=[r[1] for r in ranges],
    size=(num_samples_normali, len(ranges))
)

# Usa il modello per fare previsioni sui dati normali generati
predizioni_normali = model.predict(dati_normali)

print("Predizioni sui dati normali generati:", predizioni_normali)

# Converti i dati generati e le predizioni in un DataFrame per utilizzo con Plotly
df = pd.DataFrame(dati_normali, columns=[f'Feature {i+1}' for i in range(12)])
df['Anomaly'] = np.where(predizioni_normali == -1, 'Outlier', 'Inlier')

# Crea un grafico scatter interattivo in 3D con Plotly
fig = px.scatter_3d(df, x='Feature 1', y='Feature 2', z='Feature 3', color='Anomaly',
                    title="Predizioni di Anomalie su Dati Simulati",
                    labels={'Anomaly': 'Tipo'},
                    category_orders={"Anomaly": ["Inlier", "Outlier"]})  # Assicura un ordine consistente per i colori

# Mostra il grafico
fig.show()

# Specifica il percorso in cui vuoi salvare il file CSV
output_file_path = 'C:\\Users\\J\\Desktop\\cybersec-prototype\\predizioni_dati_normali.csv'

# Esporta il DataFrame in un file CSV
df.to_csv(output_file_path, index=False)
