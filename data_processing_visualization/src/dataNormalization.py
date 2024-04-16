import json
import pandas as pd

# Load the JSON data
with open('data_processing_visualization\src\simulated_data_5.json', 'r') as file:
    sensor_data = json.load(file)

# Create a DataFrame from the sensor data
dataframe = pd.DataFrame(sensor_data)

# Round the input temperature and humidity values to two decimal places
dataframe['temperature'] = dataframe['temperature'].round(decimals=2)
dataframe['humidity'] = dataframe['humidity'].round(decimals=2)

# Round the input temperature and humidity values to two decimal places
dataframe['temperature'] = dataframe['temperature'].round(decimals=2)
dataframe['humidity'] = dataframe['humidity'].round(decimals=2)

# Extract features (temperature and humidity) from the DataFrame
features = dataframe[['temperature', 'humidity']]

# Convert the DataFrame back to a list of dictionaries
cleaned_sensor_data = dataframe.to_dict(orient='records')

# Save the cleaned data to a new JSON file
with open('simulated_data_5.json', 'w') as file:
with open('simulated_data_5.json', 'w') as file:
    json.dump(cleaned_sensor_data, file, indent=4)

# Print the first few cleaned entries for demonstration
print("simulated_data_5.json:")
print("simulated_data_5.json:")
print(cleaned_sensor_data[:5])
