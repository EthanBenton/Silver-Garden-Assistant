import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(0)
temp = 2 * np.random.rand(100, 1)  # Generate 100 random values between 0 and 2
humid = 4 + 3 * temp + np.random.randn(100, 1)  # y = 4 + 3x + noise

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(temp, humid)

# Make predictions
humid_pred = model.predict(temp)

# Plot the data and the regression line
plt.scatter(temp, humid, color='blue', label='Actual')
plt.plot(temp, humid_pred, color='red', label='Predicted')
plt.xlabel('Temp°C')
plt.ylabel('Humidity')
plt.title('Linear Regression')
plt.legend()
plt.show()

# Evaluate the model
mse = mean_squared_error(humid, humid_pred)
print("Mean Squared Error (MSE):", mse)
