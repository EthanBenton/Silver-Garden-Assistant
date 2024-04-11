import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error


with open('data_processing_visualization/src/normalized_sensor_data.json', 'r') as file:
    normalized_data = json.load(file)

# Generate some random data for demonstration
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Generate 100 random values between 0 and 2
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the normalized training data
model.fit(X_train_normalized, y_train)

# Make predictions on the normalized testing data
y_pred = model.predict(X_test_normalized)

# Plot the predictions
plt.scatter(X_test, y_test, color='b', label='Actual')
plt.plot(X_test, y_pred, color='k', label='Predicted')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Linear Regression Prediction')
plt.legend()
plt.show()

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
