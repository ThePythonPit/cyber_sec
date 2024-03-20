import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load

import numpy as np
from joblib import load

# Carica il modello salvato
model = load('isolation_forest_model.joblib')

num_samples_normali = 20  # Numero di esempi da generare

# Assumi di generare dati con 12 caratteristiche, qui specifichiamo range ipotetici per ciascuna
# Nota: dovresti adeguare questi range in base alla conoscenza che hai delle tue caratteristiche
ranges = [(-2, 2) for _ in range(12)]  # Esempio: range ipotetici per 12 caratteristiche

# Generazione di dati normali basata su range specifici
dati_normali = np.random.uniform(
    low=[r[0] for r in ranges],
    high=[r[1] for r in ranges],
    size=(num_samples_normali, len(ranges))
)

# Usa il modello per fare previsioni sui dati normali generati
predizioni_normali = model.predict(dati_normali)

print("Predizioni sui dati normali generati:", predizioni_normali)
