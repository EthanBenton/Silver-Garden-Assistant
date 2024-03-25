import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(42)

# Define the parameters for the simulation
num_days = 30
mean_temperature = 25  # Mean temperature in degrees Celsius
temperature_variation = 5  # Variation around the mean

# Generate random temperatures for each day
random_temperatures_celsius = np.random.normal(loc=mean_temperature, scale=temperature_variation, size=num_days)

# Makes sure that temperatures are non-negative 
random_temperatures_celsius = np.maximum(random_temperatures_celsius, 0)

# Convert temperatures from Celsius to Fahrenheit
random_temperatures_fahrenheit = (random_temperatures_celsius * 9/5) + 32

# Plot the simulated temperatures in Fahrenheit
plt.plot(random_temperatures_fahrenheit, marker='o')
plt.title('Simulated Daily Temperatures for Gardening')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.show()

# Temperature Statistics    
mean_temp = np.mean(random_temperatures_fahrenheit)
median_temp = np.median(random_temperatures_fahrenheit)
min_temp = np.min(random_temperatures_fahrenheit)
max_temp = np.max(random_temperatures_fahrenheit)

# Print the Temperature Statistics
print("Temperature Statistics:")
print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Minimum Temperature:", min_temp)
print("Maximum Temperature:", max_temp)