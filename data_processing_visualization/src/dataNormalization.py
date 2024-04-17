import json
import pandas as pd

# Load the JSON data
with open('data_processing_visualization\src\simulated_data_day.json', 'r') as file:
    sensor_data = json.load(file)

# Create a DataFrame from the sensor data
dataframe = pd.DataFrame(sensor_data)

# Perform data aggregation: Calculate the average temperature and humidity for every 5 readings
aggregated_data = []

for i in range(0, len(dataframe), 5):
    # Extract the data slice
    data_slice = dataframe.iloc[i:i + 5]
    
    # Calculate the average temperature and humidity
    avg_temperature = data_slice['temperature'].mean().round(2)
    avg_humidity = data_slice['humidity'].mean().round(2)

    # Use the timestamp of the first entry in the slice as the representative timestamp
    avg_timestamp = data_slice.iloc[0]['timestamp']
    
    # Create a dictionary for the aggregated data
    aggregated_entry = {
        "humidity": avg_humidity,
        "temperature": avg_temperature,
        "timestamp": avg_timestamp
    }
    
    # Append the dictionary to the list
    aggregated_data.append(aggregated_entry)


# Save the aggregated data to a JSON file
with open('data_processing_visualization/src/aggregated_simulated_data_day.json', 'w') as output_file:
    json.dump(aggregated_data, output_file, indent=4)

# Print a success message
print("Aggregated data exported to 'data_processing_visualization/src/aggregated_simulated_data_day.json'.")









