import json
import numpy as np
import matplotlib.pyplot as plt

# Read JSON file
with open('data-input-sim\src\sensor_data.json', 'r') as file:
    data = json.load(file)

# Extract temperature and humidity data
temperatures = [entry['temperature'] for entry in data]
humidities = [entry['humidity'] for entry in data]

# Define number of bins
num_bins = 100

# Bin the data
temperature_bins = np.linspace(min(temperatures), max(temperatures), num_bins)
humidity_bins = np.linspace(min(humidities), max(humidities), num_bins)

temperature_binned = np.histogram(temperatures, bins=temperature_bins)
humidity_binned = np.histogram(humidities, bins=humidity_bins)

# Plot binned data
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(temperature_binned[1][:-1], temperature_binned[0], color='blue')
plt.title('Temperature Data')
plt.xlabel('Temperature')
plt.ylabel('Frequency')

plt.subplot(2, 1, 2)
plt.plot(humidity_binned[1][:-1], humidity_binned[0], color='green')
plt.title('Humidity Data')
plt.xlabel('Humidity')
plt.ylabel('Frequency')

plt.tight_layout()
# Show the plot

# Save the plot as an image file
image_path = 'user-interface/src/flask/static/plots/temperature_humidity_plot.png'
plt.savefig(image_path)

# Print the image path to be used in the Flask template
print(image_path)