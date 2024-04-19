import json
import numpy as np
import pandas as pd
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load data from JSON file
with open('data_processing_visualization/src/simulated_data_day.json', 'r') as f:
    raw_data = json.load(f)

num_readings = len(raw_data)

temperatures = np.empty(num_readings, dtype=np.double)
humidity = np.empty(num_readings, dtype=np.double)

# Extract humidity and temperatures from sensor data
for idx, reading in enumerate(raw_data):
    temperatures[idx] = reading["temperature"]
    humidity[idx] = reading["humidity"]

# Create DataFrame
df = pd.DataFrame({'Humidity': humidity, 'Temperature': temperatures})

# Scale the features to match the range of 0-100 for humidity and 0-100 degrees Celsius for temperature
scaler = MinMaxScaler(feature_range=(0, 100))
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Calculate slope (m) and y-intercept (b) using linear least squares approximation
x0, y0 = df_scaled['Temperature'].iloc[0], df_scaled['Humidity'].iloc[0]
x1, y1 = df_scaled['Temperature'].iloc[-1], df_scaled['Humidity'].iloc[-1]
m = (y1 - y0) / (x1 - x0)
b = y0 - m * x0

# Predict humidity based on temperature using linear least squares approximation
y_pred_least_squares = m * df_scaled['Temperature'] + b

# Plot linear least squares approximation
plt.figure(figsize=(8, 6))
plt.scatter(df_scaled['Temperature'], df_scaled['Humidity'], color='blue', label='Actual', alpha=0.5)  # Scatter plot for actual data points
plt.plot(df_scaled['Temperature'], y_pred_least_squares, color='red', label='Linear Least Squares Approximation')
plt.title('Linear Least Squares Approximation - Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.xlim(0, 50)
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()

# Fit k-means clustering model
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
kmeans.fit(df_scaled)

# Predict cluster labels
cluster_labels = kmeans.predict(df_scaled)

# Plot k-means clustering
plt.figure(figsize=(8, 6))
plt.scatter(df_scaled['Temperature'], df_scaled['Humidity'], c=cluster_labels, cmap='viridis', label='Data Points')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', c='red', label='Cluster Centers')
plt.title('K-Means Clustering')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.xlim(0, 50)
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()

# Fit RANSAC linear regression model
ransac = RANSACRegressor(LinearRegression(), random_state=0)
ransac.fit(df_scaled[['Temperature']], df_scaled['Humidity'])

# Predict humidity based on temperature using RANSAC
y_pred_ransac = ransac.predict(df_scaled[['Temperature']])

# Fit polynomial regression model
degree = 2  # Specify the degree of the polynomial
poly_features = np.column_stack([df_scaled['Temperature'] ** i for i in range(degree + 1)])
poly_reg = LinearRegression()
poly_reg.fit(poly_features, df_scaled['Humidity'])

# Predict humidity based on temperature using polynomial regression
y_pred_poly = poly_reg.predict(poly_features)

# Calculate and print mean absolute error and mean squared error for polynomial regression
mae_poly = mean_absolute_error(df_scaled['Humidity'], y_pred_poly)
mse_poly = mean_squared_error(df_scaled['Humidity'], y_pred_poly)
print("\nPolynomial Regression (Degree", degree, ") - Temperature to Humidity:")
print("Mean Absolute Error:", mae_poly)
print("Mean Squared Error:", mse_poly)




plt.figure(figsize=(8, 6))
plt.scatter(df_scaled['Temperature'], df_scaled['Humidity'], color='blue', label='Actual', alpha=0.5)  # Scatter plot for actual data points
plt.plot(df_scaled['Temperature'], y_pred_ransac, color='orange', label='Predicted (RANSAC)')
plt.title('Regression Models - Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.xlim(0, 50)  # Set x-axis limit to 0-50
plt.xticks(np.arange(0, 51, 10))  # Set x-axis tick marks
plt.yticks(np.arange(0, 101, 20))  # Set y-axis tick marks
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df_scaled['Temperature'], df_scaled['Humidity'], color='blue', label='Actual', alpha=0.5)  # Scatter plot for actual data points
plt.plot(df_scaled['Temperature'], y_pred_poly, color='green', label='Predicted (Polynomial Regression)')
plt.title('Regression Models - Temperature vs Humidity (Polynomial Regression)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.xlim(0, 50)  # Set x-axis limit to 0-50
plt.xticks(np.arange(0, 51, 10))  # Set x-axis tick marks
plt.yticks(np.arange(0, 101, 20))  # Set y-axis tick marks
plt.legend()
plt.grid(True)
plt.show()


