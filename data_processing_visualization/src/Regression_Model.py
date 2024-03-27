import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the JSON data
with open('data_input_sim/src/sensor_data.json', 'r') as file:
    sensor_data = json.load(file)

# Extract temperature and humidity data
temperatures = [entry['temperature'] for entry in sensor_data]
humidities = [entry['humidity'] for entry in sensor_data]

# Convert data to numpy arrays
X = np.array(temperatures).reshape(-1, 1)  # Reshape to a column vector
y = np.array(humidities)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict humidity values using the model
predicted_humidities = model.predict(X)

# Plot the data and the linear regression line
plt.scatter(temperatures, humidities, color='blue', label='Actual Data')
plt.plot(temperatures, predicted_humidities, color='red', label='Linear Regression')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity with Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
