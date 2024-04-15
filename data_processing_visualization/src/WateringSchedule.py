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

watering_schedule_df.to_html('watering_schedule.html', index = False)