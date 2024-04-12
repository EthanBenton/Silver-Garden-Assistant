import unittest
import json
import numpy as np
import sys
sys.path.append('data_processing_visualization\\src')
from htmlData import read_data, processData, makehtml

class TestJsonProcess(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {
            "timestamp": "2024-03-26 00:00:00",
            "temperature": 25.55,
            "humidity": 60.32
            },
            {
            "timestamp": "2024-03-26 00:10:00",
            "temperature": 26.56,
            "humidity": 65.94
            },
            {
            "timestamp": "2024-03-26 00:20:00",
            "temperature": 25.73,
            "humidity": 63.21
            },
        ]
        with open('example.json', 'w' ) as file:
            json.dump(self.sample_data, file)
    
    def test_read_data(self):
        data = read_data('example.json')
        self.assertEqual(data, self.sample_data)

    def test_processData(self):
        temperature, temperatureCount, humidity, humidityCount, timestamp = processData(self.sample_data)
        
        self.assertEqual(len(temperature), len(self.sample_data))
        self.assertEqual(len(humidity), len(self.sample_data))
        self.assertEqual(len(timestamp), len(self.sample_data))

        for temp, humid in zip(temperature, humidity):
            self.assertFalse(isinstance(temp, float) or isinstance(temp, int))
            self.assertFalse(isinstance(humid, float) or isinstance(humid, int))

    def tearDown(self):
        import os
        os.remove('example.json')
        
if __name__ == '__main__':
    unittest.main()