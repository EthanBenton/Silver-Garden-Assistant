import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json
from datetime import datetime

# Assuming you have pulled gardening data from a database and stored it in a DataFrame called gardening_data
# Here's a sample DataFrame with dummy data
data = {
    'temperature': (30, 25, 20, 15, 35),
    'humidity': (60, 50, 45, 55, 65),
    
}
gardening_data = pd.DataFrame(data)

# Display original data
print("Original Preprocessing Data:")
print(gardening_data)

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# List of columns to normalize
columns_to_normalize = ['temperature', 'humidity']

# Apply Min-Max scaling to the selected columns
gardening_data[columns_to_normalize] = scaler.fit_transform(gardening_data[columns_to_normalize])

# Display normalized data
print("\nNormalized Preprocessing Data:")
print(gardening_data)

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add timestamp to the data
gardening_data['timestamp'] = timestamp

# Convert DataFrame to JSON
original_data_json = gardening_data.to_json(orient='records')

# Save original preprocessing data to a JSON file
with open('original_data.json', 'w') as f:
    f.write(original_data_json)

# Display message
print("\nOriginal data saved to original_data.json")

# Convert normalized DataFrame to JSON
normalized_data_json = gardening_data.to_json(orient='records')

# Save normalized data to a JSON file
with open('normalized_data.json', 'w') as f:
    f.write(normalized_data_json)

# Display message
print("Normalized data saved to normalized_data.json")
