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
            "temperature": 20.81,
            "humidity": 43.78
            },
            {
            "timestamp": "2024-03-26 00:10:00",
            "temperature": 20.18,
            "humidity": 47.87
            },
            {
            "timestamp": "2024-03-26 00:20:00",
            "temperature": 25.54,
            "humidity": 36.73
            },
        ]
        with open('example.json', 'w' ) as file:
            json.dump(self.sample_data, file)

    def tearDown(self):
        import os
        os.remove('example.json')
    
    def test_read_data(self):
        data = read_data('example.json')
        self.assertEqual(data, self.sample_data)

if __name__ == '__main__':
    unittest.main()