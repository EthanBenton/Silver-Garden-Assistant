import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

# Load the json file
with open('simulated_data_5.json') as f:
    data = json.load(f)

# Take the timestamps, temperatures, and humidities from json file
temperatures = [entry['temperature'] for entry in data]
humidities = [entry['humidity'] for entry in data]    
timestamps = [datetime.strptime(entry['timestamp'], '%Y-%M-%D %H:%M%S') for entry in data]

# Create the dataframe from data taken from json
df = pd.DataFrame({
    'humidity': humidities,
    'temperature': temperatures,
    'timestamp': timestamps,

})

