import json
import numpy as np
import pandas as pd
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data from JSON file
with open('C:\\Users\\aamri\\Documents\\GitHub\\Silver-Garden-Assistant\\data_processing_visualization\\src\simulated_data_day.json', 'r') as f:
    raw_data = json.load(f)

data_structure = {
    "humidity": None,
    "temperature": None,
    "timestamp": None
}

num_readings = len(raw_data)

temperatures = np.empty(num_readings, dtype=np.double)
humidity = np.empty(num_readings, dtype=np.double)

# Extract temperatures and humidity from sensor data
for idx, reading in enumerate(raw_data):
    for key in data_structure:
        if key in reading:
            if key == "temperature":
                temperatures[idx] = reading[key]
            elif key == "humidity":
                humidity[idx] = reading[key]

# Create DataFrame
df = pd.DataFrame({'Temperature': temperatures, 'Humidity': humidity})

# Calculate slope (m) and y-intercept (b) using linear least squares approximation
x0, y0 = df['Temperature'].iloc[0], df['Humidity'].iloc[0]
x1, y1 = df['Temperature'].iloc[-1], df['Humidity'].iloc[-1]
m = (y1 - y0) / (x1 - x0)
b = y0 - m * x0

# Predict humidity based on temperature using linear least squares approximation
y_pred_least_squares = m * df['Temperature'] + b

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Temperature']])

num_clusters = 3

kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
kmeans.fit(X_scaled)

cluster_assignn = kmeans.labels_

cluster_centroids = kmeans.cluster_centers_

# Print cluster assignments
print("Cluster Assignments:")
for i, label in enumerate(kmeans.labels_):
    print("Data point:", df['Temperature'].iloc[i], "is assigned to cluster", label)
    print("Data point:", df['Humidity'].iloc[i], "is assigned to cluster", label)

# Print cluster centroids
print("\nCluster Centroids:")
for i, centroid in enumerate(kmeans.cluster_centers_):
    print("Cluster", i, "centroid:", centroid)

# Fit RANSAC linear regression model for predicting humidity from temperature
ransac = RANSACRegressor(LinearRegression(), random_state=0)
ransac.fit(X_scaled, df['Humidity'])

# Predict humidity based on temperature
y_pred_hum = ransac.predict(X_scaled)

# Fit polynomial regression model
degree = 2  # Specify the degree of the polynomial
poly_features = np.column_stack([X_scaled ** i for i in range(degree + 1)])
poly_reg = LinearRegression()
poly_reg.fit(poly_features, df['Humidity'])

# Predict humidity based on temperature using polynomial regression
y_pred_poly = poly_reg.predict(poly_features)

# Calculate and print mean absolute error and mean squared error for polynomial regression
mae_poly = mean_absolute_error(df['Humidity'], y_pred_poly)
mse_poly = mean_squared_error(df['Humidity'], y_pred_poly)
print("\nPolynomial Regression (Degree", degree, ") - Temperature to Humidity:")
print("Mean Absolute Error:", mae_poly)
print("Mean Squared Error:", mse_poly)

# Visualize the regression
plt.figure(figsize=(12, 6))
plt.scatter(df['Temperature'], df['Humidity'], color='blue', label='Actual', alpha=0.5)  # Scatter plot for actual data points
plt.plot(df['Temperature'], y_pred_least_squares, color='red', label='Predicted (Linear Least Squares)')
plt.title('Linear Least Squares Approximation - Temperature vs Humidity')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.legend()
plt.show()
