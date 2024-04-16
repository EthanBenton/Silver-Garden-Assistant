import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime, timedelta

# Load the json file
with open('simulated_data_5.json') as f:
    data = json.load(f)

# Take the timestamps, temperatures, and humidities from json file
temperatures = [entry['temperature'] for entry in data]
humidities = [entry['humidity'] for entry in data]    
timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]

# Create the dataframe from data taken from json
df = pd.DataFrame({
    'humidity': humidities,
    'temperature': temperatures,
    'timestamp': timestamps,

})

# Sets the timestamp as the dataframe index
df.set_index('timestamp', inplace = True)

# Change the data to 1 hour invtervals and replace missing values
df = df.resample('1h').mean().interpolate()

# Create the watering schedule based on data
df['watering_schedule'] = np.where((df['temperature'] > 25) & (df['humidity'] < 60), 1, 0)

# Makes the schedule only allow people to water once a day
df['watering_schedule'] = df['watering_schedule'].groupby(pd.Grouper(freq = 'D')).transform('max')

# Adding the days of the week with the timestamps
df['days_of_the_week'] = df.index.day_name()

# Make the days of the week
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
df['days_of_the_week'] = pd.Categorical(df['days_of_the_week'], categories = weekdays, ordered = True)

# Select the data to train
X = df[['temperature', 'humidity']]
Y = df['watering_schedule']

# Training
model = RandomForestClassifier()
model.fit(X, Y)

# Create the predictions from the data
predictions = model.predict(X)

# Create the data frame for the watering schedule
watering_schedule_df = pd.DataFrame({
    'timestamp': df.index,
    'days_of_the_week': df['days_of_the_week'],
    'watering_required': predictions
})

# Provide a time estimate of when it's best to water your plant
df['watering_time'] = np.where((df['temperature']> 25) & (df['humidity'] < 60), 'Morning', 'Evening')

# Make the table produce horizontally
watering_schedule_df = df.pivot_table(index = df.index.date, columns = 'days_of_the_week',
 values = ['watering_schedule', 'watering_time'], aggfunc = 'first', observed = False)

# Replace the 1s as Water Plant
watering_schedule_df.replace(1, 'Water Plant', inplace = True)

# Save and send the schedule to an html
watering_schedule_df.to_html('watering_schedule.html', na_rep = '', index = True)
