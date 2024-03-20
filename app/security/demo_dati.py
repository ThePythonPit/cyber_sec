



from flask import Flask
import pandas as pd
from sklearn.ensemble import IsolationForest
from joblib import load
import numpy as np


app = Flask(__name__)

# Define paths to your model and data file
MODEL_PATH = 'C:\\Users\\J\\Desktop\\cybersec-prototype\\isolation_forest_model.joblib'
DATA_PATH = 'C:\\Users\\J\\Desktop\\cybersec-prototype\\predizioni_dati_normali.csv'

# Load the model from the specified path
model = load(MODEL_PATH)

# Function to load demo data from a CSV file
def load_demo_data(file_path):
    return pd.read_csv(file_path)

# Function to process demo data and make predictions using the loaded model
def process_data_and_predict(model, demo_data):
    results = []
    print("Inizio dell'elaborazione dei dati...")  # Debug print
    
    for index, row in demo_data.iterrows():
        # Extract features based on the column names in the DataFrame
        feature_columns = [f'Feature {i}' for i in range(1, 13)]
        features = row[feature_columns].values.reshape(1, -1)
        
        # Predict using the loaded model
        prediction = model.predict(features)
        
        # Add the prediction result to the results list
        result = 'Outlier' if prediction[0] == -1 else 'Inlier'
        results.append(result)
        print(f"Prediction for row {index}: {result}")

    return results

# Define a route for your Flask app
@app.route('/')
def index():
    return "IDS Flask App is Running!"

# Load demo data
demo_data = load_demo_data(DATA_PATH)

# When the script is executed, process the data and print predictions
if __name__ == '__main__':
    predictions = process_data_and_predict(model, demo_data)
    app.run(debug=True)
