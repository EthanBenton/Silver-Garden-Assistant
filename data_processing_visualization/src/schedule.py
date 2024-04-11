import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

with open('data_input_sim/src/sensor_data.json') as f:
    data = json.load(f)
for entry in data:
    timestamps.append(entry['timestamp'])
    temperatures.append(enty['temperature'])
    humidities.append(entry['humidity'])

df = pd.DataFrame({
    'timestamp': timestamps,
    'temperature': temperatures,
    'humidity': humidities
})

df['timestamp'] = pd.to_datetime(df['timestamp'])

X = df[['humidity', 'temperature']]
Y = df['watering_schedule']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

model = RandomForestClassifier()

model.fit(X_train, Y_train)

prediction = model.predict(X_test)

accuracy = np.mean(prediction == Y_test)
print(f"Model Accuracy: {accuracy}")