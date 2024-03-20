import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from joblib import dump



# Carica il dataset
file_path = 'C:\\Users\\J\\Desktop\\cybersec-prototype\\horse_names.csv'
data = pd.read_csv(file_path)

# Controlla per valori mancanti
missing_values = data.isnull().sum()
print("Valori mancanti per colonna:\n", missing_values)

if 'timestamp' in data.columns:
    data_cleaned = data.drop(['timestamp'], axis=1)
else:
    data_cleaned = data.copy()

data_cleaned = data_cleaned.select_dtypes(include=[np.number])

# Continua con la normalizzazione e il resto del processo come prima
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_cleaned)

X_train, X_test = train_test_split(data_scaled, test_size=0.2, random_state=42)

model = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
model.fit(X_train)

y_test_pred = model.predict(X_test)
n_outliers = (y_test_pred == -1).sum()

# Salvataggio del modello addestrato su disco

print(data.columns)

dump(model, 'C:\\Users\\J\\Desktop\\cybersec-prototype\\horse_names_nuovo')
print(f"Numero di outlier identificati: {n_outliers} su {len(X_test)}")
