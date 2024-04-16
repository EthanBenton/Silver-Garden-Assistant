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
            self.data = [
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

    
