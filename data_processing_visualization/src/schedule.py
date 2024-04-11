import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

timestamps = []
temperatures = []
humidities = []

with open('data_input_sim/src/sensor_data.json') as f:
    data = json.load(f)
for entry in data:
    timestamps.append(entry['timestamp'])
    temperatures.append(entry['temperature'])
    humidities.append(entry['humidity'])

df = pd.DataFrame({
    'timestamp': timestamps,
    'temperature': temperatures,
    'humidity': humidities
})

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['watering_schedule'] = np.where((df['temperature'] >  25 ) & (df['humidity'] < 60), 1, 0)

X = df.drop(columns=['watering_schedule', 'timestamp'])

Y = df['watering_schedule']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

prediction = model.predict(X)

watering_schedule_df = pd.DataFrame({
    'timestamp': df['timestamp'], 'watering_required': prediction
})

print(watering_schedule_df)