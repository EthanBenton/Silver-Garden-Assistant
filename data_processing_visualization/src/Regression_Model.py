import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# Load the JSON data
with open('data_processing_visualization/src/sensor_data.json', 'r') as file:
    sensor_data = json.load(file)

# Extract temperature and humidity data
temperatures = np.array([entry['temperature'] for entry in sensor_data]).reshape(-1, 1)
humidities = np.array([entry['humidity'] for entry in sensor_data])

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(temperatures, humidities, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict humidity values using the model
predicted_humidities = model.predict(X_val)

# Plot the data and the linear regression line
plt.scatter(X_val, y_val, color='blue', label='Actual Data')
plt.plot(X_val, predicted_humidities, color='red', label='Linear Regression')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity with Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

# Calculate mean squared error (MSE) and R-squared
mse = mean_squared_error(y_val, predicted_humidities)
r2 = r2_score(y_val, predicted_humidities)
print("Mean Squared Error (MSE):", mse)
print("R-squared:", r2)
