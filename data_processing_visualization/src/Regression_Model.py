import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the data
raw_data = pd.read_json('data_input_sim/src/sensor_data.json')


# Extract features (X) and target variable (y) for Irrigation Control and Light exposure management
x = raw_data[['Irrigation Control Feature 1', 'Irrigation Control Feature 2',
              'Light exposure management Feature 1', 'Light exposure management Feature 2']]
y = raw_data['Light exposure management Target']  # Replace 'Target Variable' with the appropriate column name


# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Train a linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

# Print model coefficients and intercept
print('Model Coefficients:', model.coef_)
print('Model Intercept:', model.intercept_)

# Create a DataFrame to display coefficients
coefficients_df = pd.DataFrame(model.coef_, index=x.columns, columns=['Coefficient'])
print('\nCoefficient Values:')
print(coefficients_df)

# Make predictions on the testing set
predict = model.predict(x_test)

# Plot a histogram of the residuals using matplotlib
plt.figure(figsize=(8, 6))
plt.hist(y_test - predict, bins=20, color='skyblue', alpha=0.75)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')
plt.grid(True)
plt.show()

# Plot residuals using seaborn
plt.figure(figsize=(8, 6))
sns.histplot(y_test - predict, bins=20, color='skyblue', kde=True)
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.title('Histogram of Residuals (Seaborn)')
plt.grid(True)
plt.show()

# Calculate evaluation metrics
from sklearn import metrics
print('\nEvaluation Metrics:')
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, predict))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, predict))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, predict)))
