import numpy as np
import pandas as pd

# Load plant data from CSV into a pandas DataFrame
def load_gardening_data(file_path):
    return pd.read_csv(file_path)

# A function for data processing and analysis
def process_gardening_data(df):
    # Example data processing and analysis
    # Calculate mean height
    mean_height = df['Height (cm)'].mean()

    # Sort it by watering frequency 
    df_sorted = df.sort_values(by='Watering Frequency (days)')
    
     