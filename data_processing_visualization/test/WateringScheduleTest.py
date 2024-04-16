import unittest
import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime, timedelta
import sys
sys.path.append('data_processing_visualization\\src\\')
from WateringSchedule import *

class TestWaterSchedule(unittest.TestCase):

    # Test the opening of a test json file
    def setUp(self):
        self.sample_data = [
            {
                "humidity": 46.12,
                "temperature": 24.46,
                "timestamp": "2024-04-11 20:56:49"
            },
            {
                "humidity": 54.6,
                "temperature": 26.06,
                "timestamp": "2024-04-11 20:57:49"
            },
            {
                "humidity": 45.0,
                "temperature": 27.77,
                "timestamp": "2024-04-11 20:58:49"
            },
            {
                "humidity": 61.95,
                "temperature": 24.37,
                "timestamp": "2024-04-11 20:59:49"
            },
            {
                "humidity": 56.19,
                "temperature": 28.81,
                "timestamp": "2024-04-11 21:00:49"
            }
        ]

        # Make a sample data frame
        self.sample_df = pd.DataFrame(self.sample_data)
        self.sample_df['timestamp'] = pd.to_datetime(self.sample_df['timestamp'])
        self.sample_df.set_index('timestamp', inplace = True)

    # Test if the json file will load
    def test_load_json(self):
        self.assertTrue(isinstance(self.sample_data, list))

    # Test if the data frame was made
    def test_dataframe_creation(self):
        self.assertTrue(isinstance(sample.data_df, pd.DataFrame))

    # Test the resampling and interpolation
    def test_resample_and_interpolation(self):
        resample_df = test_resample_and_interpolation(self.sample_df)
        self.assertEqual(len(resample_df), 5)

    # Test the watering schedule prediction
    def test_watering_schedule_prediction(self):
        X_test = self.sample_df[['temperature', 'humidity']]
        predictions = predict_watering_schedule(X_test)
        self.assertEqual(len(predictions), len(self.sample_data_df))

    # Test the watering time estimation
    def test_watering_time_estimation(self):
        estimated_time = estimate_watering_time(self.sample_df)
        self.assertEqual(len(estimated_time), len(self.sample_data_df))

    # Test the the schedule generator
    def test_watering_schedule_generation(self):
        generate_watering_schedule_html(self.sample_df)

if __name__ == '__main__':
    unittest.main()