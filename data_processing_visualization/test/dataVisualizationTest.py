import unittest
from unittest.mock import patch
import json
import numpy as np

def read_sensor_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def generate_simulated_data(num_days, mean_temperature, temperature_variation):
    np.random.seed(42)
    random_temperatures_celsius = np.random.normal(loc=mean_temperature, scale=temperature_variation, size=num_days)
    random_temperatures_celsius = np.maximum(random_temperatures_celsius, 0)
    random_temperatures_fahrenheit = (random_temperatures_celsius * 9/5) + 32
    return random_temperatures_fahrenheit

def calculate_statistics(temperatures):
    mean_temp = np.mean(temperatures)
    median_temp = np.median(temperatures)
    min_temp = np.min(temperatures)
    max_temp = np.max(temperatures)
    return mean_temp, median_temp, min_temp, max_temp

class TestDataProcessing(unittest.TestCase):

    @patch('builtins.open', side_effect=[
        json.dumps([
            {"timestamp": "2022-01-01", "temperature": 20},
            {"timestamp": "2022-01-02", "temperature": 22},
            {"timestamp": "2022-01-03", "temperature": 24},
            # More sensor data entries...
        ])
    ])
    def test_read_sensor_data(self, mock_open):
        file_path = 'data-processing-visualization/src/sensor_data.json'
        data = read_sensor_data(file_path)
        self.assertEqual(data, [
            {"timestamp": "2022-01-01", "temperature": 20},
            {"timestamp": "2022-01-02", "temperature": 22},
            {"timestamp": "2022-01-03", "temperature": 24},
            # More sensor data entries...
        ])

    def test_generate_simulated_data(self):
        num_days = 30
        mean_temperature = 25
        temperature_variation = 5
        simulated_data = generate_simulated_data(num_days, mean_temperature, temperature_variation)
        self.assertEqual(len(simulated_data), num_days)

    def test_calculate_statistics(self):
        temperatures = [20, 22, 24, 26, 28]
        mean_temp, median_temp, min_temp, max_temp = calculate_statistics(temperatures)
        self.assertEqual(mean_temp, np.mean(temperatures))
        self.assertEqual(median_temp, np.median(temperatures))
        self.assertEqual(min_temp, np.min(temperatures))
        self.assertEqual(max_temp, np.max(temperatures))

if __name__ == '__main__':
    unittest.main()