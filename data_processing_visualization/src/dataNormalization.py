import json
import pandas as pd
import matplotlib.pyplot as plt

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

# Create a DataFrame from the aggregated data
aggregated_dataframe = pd.DataFrame(aggregated_data)

# Calculate quartiles and IQR for temperature and humidity
temperature_q1 = aggregated_dataframe['temperature'].quantile(0.25)
temperature_q3 = aggregated_dataframe['temperature'].quantile(0.75)
temperature_iqr = temperature_q3 - temperature_q1

humidity_q1 = aggregated_dataframe['humidity'].quantile(0.25)
humidity_q3 = aggregated_dataframe['humidity'].quantile(0.75)
humidity_iqr = humidity_q3 - humidity_q1

# Print quartiles and IQR for temperature
print("Temperature Quartiles:")
print(f"Q1: {temperature_q1:.2f}")
print(f"Q3: {temperature_q3:.2f}")
print(f"IQR: {temperature_iqr:.2f}")

# Print quartiles and IQR for humidity
print("\nHumidity Quartiles:")
print(f"Q1: {humidity_q1:.2f}")
print(f"Q3: {humidity_q3:.2f}")
print(f"IQR: {humidity_iqr:.2f}")

# Plot a box plot for temperature and humidity with annotations for quartiles and IQR
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)  # Creating subplots side by side
plt.boxplot(aggregated_dataframe['temperature'])
plt.title('Temperature')
plt.ylabel('Temperature (°C)')
plt.ylim(0, 50)
plt.text(0.85, temperature_q1, f'Q1: {temperature_q1:.2f}', va='center', ha='center', backgroundcolor='w')
plt.text(0.85, temperature_q3, f'Q3: {temperature_q3:.2f}', va='center', ha='center', backgroundcolor='w')
plt.text(0.85, temperature_q1 - 0.5, f'IQR: {temperature_iqr:.2f}', va='center', ha='center', backgroundcolor='w')

plt.subplot(1, 2, 2)
plt.boxplot(aggregated_dataframe['humidity'], showfliers=True)
plt.title('Humidity')
plt.ylabel('Humidity (%)')
plt.ylim(0, 100) 
plt.text(0.85, humidity_q1, f'Q1: {humidity_q1:.2f}', va='center', ha='center', backgroundcolor='w')
plt.text(0.85, humidity_q3, f'Q3: {humidity_q3:.2f}', va='center', ha='center', backgroundcolor='w')
plt.text(0.85, humidity_q1 - 2, f'IQR: {humidity_iqr:.2f}', va='center', ha='center', backgroundcolor='w')

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()



# Print a success message
print("Aggregated data exported to 'data_processing_visualization/src/aggregated_simulated_data_day.json'.")









