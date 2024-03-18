import unittest
import json
import numpy as np
import matplotlib.pyplot as plt

def process_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    temperatures = [entry['temperature'] for entry in data]
    humidities = [entry['humidity'] for entry in data]

    num_bins = 100

    temperature_bins = np.linspace(min(temperatures), max(temperatures), num_bins)
    humidity_bins = np.linspace(min(humidities), max(humidities), num_bins)

    temperature_binned = np.histogram(temperatures, bins=temperature_bins)
    humidity_binned = np.histogram(humidities, bins=humidity_bins)

    return temperature_binned, humidity_binned

class TestDataProcessing(unittest.TestCase):
    def test_data_processing(self):
        filename = 'data-input-sim\src\sensor_data.json'
        temperature_binned, humidity_binned = process_data(filename)

        self.assertEqual(len(temperature_binned), 2)
        self.assertEqual(len(humidity_binned), 2)

        self.assertEqual(len(temperature_binned[0]), len(temperature_binned[1]) - 1)
        self.assertEqual(len(humidity_binned[0]), len(humidity_binned[1]) - 1)

        self.assertTrue(np.all(temperature_binned[0] >= 0))
        self.assertTrue(np.all(humidity_binned[0] >= 0))

if __name__ == '__main__':
    unittest.main()