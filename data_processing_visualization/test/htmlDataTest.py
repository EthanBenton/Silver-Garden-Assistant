import unittest
import json
import numpy as np
import sys
sys.path.append('data_processing_visualization\\src')
from htmlData import *

class TestJsonProcess(unittest.TestCase):

    # Sample data
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
        # Write the sample data to a file
        with open('example.json', 'w' ) as file:
            json.dump(self.sample_data, file)
    
    def test_read_data(self):
        data = read_data('example.json')
        self.assertEqual(data, self.sample_data)

    def test_processData(self):
        temperature, temperatureCount, humidity, humidityCount, timestamp = processData(self.sample_data)
        
        # Makes sure the arrays are the right length
        self.assertEqual(len(temperature), len(self.sample_data))
        self.assertEqual(len(humidity), len(self.sample_data))
        self.assertEqual(len(timestamp), len(self.sample_data))

        # Makes sure the temperature and humidity are floats or integers
        for temp, humid in zip(temperature, humidity):
            self.assertFalse(isinstance(temp, float) or isinstance(temp, int))
            self.assertFalse(isinstance(humid, float) or isinstance(humid, int))

    # Remove the temporary file
    def tearDown(self):
        import os
        os.remove('example.json')
        
    def test_makehtml(self):
        # Sample data
        temperature = [25, 26, 25]
        temperatureCount = {25: 2, 26: 1}
        humidity = [60, 65, 63]
        humidityCount = {60: 1, 65: 1, 63: 1}
        timestamp = ['2024-03-26 00:00:00', '2024-03-26 00:10:00', '2024-03-26 00:20:00']

        # Make an output file
        output_file = 'test_output.html'

        # Call output file function
        makehtml(temperature, temperatureCount, humidity, humidityCount, timestamp, output_file)


        # Read the output file
        with open(output_file, 'r') as f:
            html_content = f.read()

        # Make certain parts of the html file strings are in the file
        self.assertIn('<h1>Processed Data</h1>', html_content)
        self.assertIn('<h2> Temperature</h2>', html_content)
        self.assertIn('<h2> Humidity</h2>', html_content)

        # Remove the temporary file
        import os
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()