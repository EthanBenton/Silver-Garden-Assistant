import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime, timedelta

def load_sensor_data(file_path: str) -> dict:
    """
    Load sensor data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: Dictionary containing sensor data.
    """
    with open(file_path) as f:
        data = json.load(f)
    return data

def create_dataframe(data: dict) -> pd.DataFrame:
    """
    Create a Pandas data frame from sensor data.
    
    Args:
        data (dict): Dictionary containing sensor data.
    
    Returns:
        pd.DataFrame: Data frame containing sensor data.
    """
    temperatures = [entry['temperature'] for entry in data]
    humidities = [entry['humidity'] for entry in data]
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]
    
    df = pd.DataFrame({
        'humidity': humidities,
        'temperature': temperatures,
        'timestamp': timestamps,
    })
    df.set_index('timestamp', inplace=True)
    df = df.resample('1h').mean().interpolate()
    return df

def create_watering_schedule(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a watering schedule based on temperature and humidity data.
    
    Args:
        df (pd.DataFrame): Data frame containing temperature and humidity data.
    
    Returns:
        pd.DataFrame: Data frame containing watering schedule.
    """
    df['watering_schedule'] = np.where((df['temperature'] > 25) & (df['humidity'] < 60), 1, 0)
    df['watering_schedule'] = df['watering_schedule'].groupby(pd.Grouper(freq='D')).transform('max')
    df['days_of_the_week'] = df.index.day_name()
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    df['days_of_the_week'] = pd.Categorical(df['days_of_the_week'], categories = weekdays, ordered = True)
    return df

def train_model(df: pd.DataFrame) -> RandomForestClassifier:
    """
    Train a random forest classifier model.
    
    Args:
        df (pd.DataFrame): Data frame containing training data.
    
    Returns:
        RandomForestClassifier: Trained random forest classifier model.
    """
    X = df[['temperature', 'humidity']]
    Y = df['watering_schedule']
    model = RandomForestClassifier()
    model.fit(X, Y)
    return model

def create_watering_schedule_df(df: pd.DataFrame, model: RandomForestClassifier) -> pd.DataFrame:
    """
    Create a data frame for the watering schedule based on predictions.
    
    Args:
        df (pd.DataFrame): Data frame containing sensor data.
        model (RandomForestClassifier): Trained random forest classifier model.
    
    Returns:
        pd.DataFrame: Data frame containing watering schedule predictions.
    """
    predictions = model.predict(df[['temperature', 'humidity']])
    watering_schedule_df = pd.DataFrame({
        'timestamp': df.index,
        'days_of_the_week': df['days_of_the_week'],
        'watering_required': predictions
    })
    return watering_schedule_df

def generate_watering_time(df: pd.DataFrame) -> None:
    """
    Provide a time estimate of when it's best to water the plant.
    
    Args:
        df (pd.DataFrame): Data frame containing sensor data.
    
    Returns:
        None
    """
    df['watering_time'] = np.where((df['temperature'] > 25) & (df['humidity'] < 60), 'Morning', 'Evening')

def generate_watering_schedule_html(df: pd.DataFrame, file_path: str) -> None:
    """
    Generate and save the watering schedule as an HTML file.
    
    Args:
        df (pd.DataFrame): Data frame containing watering schedule.
        file_path (str): Path to save the HTML file.
    
    Returns:
        None
    """
    watering_schedule_df = df.pivot_table(index=df.index.date, columns = 'days_of_the_week',
        values = ['watering_schedule', 'watering_time'], aggfunc = 'first', observed = False)
    watering_schedule_df.replace(1, 'Water Plant', inplace = True)
    watering_schedule_df.to_html(file_path, na_rep = '', index = True)

# Load sensor data
data = load_sensor_data('user_interface\\src\\flask\\static\\data\\simulated_data_week.json')

# Create DataFrame
df = create_dataframe(data)

# Create watering schedule
df = create_watering_schedule(df)

# Train model
model = train_model(df)

# Create DataFrame for watering schedule
watering_schedule_df = create_watering_schedule_df(df, model)

# Provide watering time estimate
generate_watering_time(df)

# Generate and save watering schedule as HTML
generate_watering_schedule_html(df, 'user_interface\\src\\frontend\\public\\graphs\\watering_schedule.html')