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

    # Test loading the json
    def test_load_from_json(self):
        data = json.load(f)
        self.assertEqual(len(data), 3)
        self.assertIn("humidity", data[0])
        self.assertIn("temperature", data[0])
        self.assertIn("timestamp", data[0])

    # Test creating a data frame from json
    def test_create_dataframe(self):
        test_humidity = [entry['humidity'] for entry in self.sample_data]
        test_temperature = [entry['temperature'] for entry in self.sample_data]
        test_timestamp = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in self.sample_data]

    # Create data frame from data
        df = pd.DataFrame({
            'humidity': test_humidity,
            'temperature': test_temperature,
            'timestamp': test_timestamp
        })
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 3)
        self.assertEqual(list(df.columns), ['humidity', 'temperature', 'timestamp'])
        self.assertEqual(df['timestamp'].dtype, '<M8[ns]')
        
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
        ]

        # Write data to temporary json file
        with open('sample_data.json', 'w') as f:
            json.dump(self.sample_data, f)

        def tearDown(self):
            import os
            os.remove('sample_data.json')

if __name__ == '__main__':
    unittest.main()