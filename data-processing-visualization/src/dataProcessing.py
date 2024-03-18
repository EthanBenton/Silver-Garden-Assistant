import json
import numpy as np
import matplotlib.pyplot as plt

# Read the Json file
def read_sensor_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Generate the simulated daily temperatures
def generate_simulated_data(num_days, mean_temperature, temperature_variation):
    np.random.seed(42)
    random_temperatures_celsius = np.random.normal(loc=mean_temperature, scale=temperature_variation, size=num_days)
    random_temperatures_celsius = np.maximum(random_temperatures_celsius, 0)
    random_temperatures_fahrenheit = (random_temperatures_celsius * 9/5) + 32
    return random_temperatures_fahrenheit

# Plot the temperatures
def plot_temperatures(temperatures, title):
    plt.plot(temperatures, marker='o')
    plt.title(title)
    plt.xlabel('Day')
    plt.ylabel('Temperature (°F)')
    plt.show()

# Calculate the temperature statistics
def calculate_statistics(temperatures):
    mean_temp = np.mean(temperatures)
    median_temp = np.median(temperatures)
    min_temp = np.min(temperatures)
    max_temp = np.max(temperatures)
    return mean_temp, median_temp, min_temp, max_temp

# Reads sensor data
file_path = 'data-processing-visualization/src/sensor_data.json'
sensor_data = read_sensor_data(file_path)

# Set parameters for simulation
num_days = 30
mean_temperature = 25  # Mean temperature in degrees Celsius
temperature_variation = 5  # Variation around the mean

# Generate simulated temperatures
simulated_temperatures = generate_simulated_data(num_days, mean_temperature, temperature_variation)

# Plot simulated temperatures
plot_temperatures(simulated_temperatures, 'Simulated Daily Temperatures for Gardening')

# Calculate statistics for simulated temperatures
mean_temps_sim, median_temps_sim, min_temps_sim, max_temps_sim = calculate_statistics(simulated_temperatures)

# Print the Temperature Statistics for simulated temperatures
print("Temperature Statistics for Simulated Data:")
print("Mean Temperature:", mean_temps_sim)
print("Median Temperature:", median_temps_sim)
print("Minimum Temperature:", min_temps_sim)
print("Maximum Temperature:", max_temps_sim)

# If sensor data is available, process and analyze it
if sensor_data:
    # Extract temperatures from sensor data
    sensor_temperatures = [entry['temperature'] for entry in sensor_data]

    # Plot sensor temperatures
    plot_temperatures(sensor_temperatures, 'Sensor Daily Temperatures')

    # Calculate statistics for sensor temperatures
    mean_temp_sensor, median_temp_sensor, min_temp_sensor, max_temp_sensor = calculate_statistics(sensor_temperatures)

    # Prints the Temperature Statistics for sensor data
    print("\nTemperature Statistics for Sensor Data:")
    print("Mean Temperature:", mean_temp_sensor)
    print("Median Temperature:", median_temp_sensor)
    print("Minimum Temperature:", min_temp_sensor)
    print("Maximum Temperature:", max_temp_sensor)
else:
    print("\nSensor data not available.")