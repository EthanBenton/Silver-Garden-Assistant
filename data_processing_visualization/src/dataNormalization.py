import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the JSON data
with open('data_processing_visualization/src/sensor_data.json', 'r') as file:
    sensor_data = json.load(file)

# Create a DataFrame from the sensor data
dataframe = pd.DataFrame(sensor_data)

# Extract features (temperature and humidity) from the DataFrame
features = dataframe[['temperature', 'humidity']]

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler to the data and transform the data
normalized_data = scaler.fit_transform(features)

# Round the normalized data to have two decimal places using NumPy
rounded_data = np.round(normalized_data, decimals=2)

# Update the DataFrame with the rounded values
dataframe[['temperature', 'humidity']] = rounded_data

# Convert the DataFrame back to a list of dictionaries
cleaned_sensor_data = dataframe.to_dict(orient='records')

# Save the cleaned data to a new JSON file
with open('cleaned_sensor_data.json', 'w') as file:
    json.dump(cleaned_sensor_data, file, indent=4)

# Print the first few cleaned entries for demonstration
print("Cleaned Sensor Data:")
print(cleaned_sensor_data[:5])








