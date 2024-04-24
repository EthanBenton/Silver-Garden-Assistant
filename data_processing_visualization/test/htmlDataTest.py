import unittest
import json
import numpy as np
import sys
sys.path.append('data_processing_visualization/src')
from htmlData import htmlData

class htmlDataTest(unittest.TestCase):

    def setUp(self):
        """
        Create a temporary json file for testing
        """
        self.test_data = [
            {"humidity": 46.11708606933448, "temperature": 24.463786814431522, "timestamp": "2024-04-11 20:56:49"},
            {"humidity": 54.59773018104158, "temperature": 26.059561397324842, "timestamp": "2024-04-11 20:57:49"}
        ]
        with open("test_data.json", "w") as f:
            json.dump(self.test_data, f)

    def test_read_data(self):
        """
        Test read_data method
        """
        html_data = htmlData()
        data = html_data.read_data("test_data.json")
        self.assertEqual(data, self.test_data)

    def test_process_data(self):
        """
        Test processData method
        """
        html_data = htmlData()
        humidity, humidity_count, temperature, temperature_count, timestamp = html_data.processData(self.test_data)
        
        expected_humidity = np.array([46, 55])
        expected_humidity_count = {46: 1, 55: 1}
        expected_temperature = np.array([24, 26])
        expected_temperature_count = {24: 1, 26: 1}
        expected_timestamp = ['2024-04-11 20:56:49', '2024-04-11 20:57:49']

        np.testing.assert_array_equal(humidity, expected_humidity)
        self.assertEqual(humidity_count, expected_humidity_count)
        np.testing.assert_array_equal(temperature, expected_temperature)
        self.assertEqual(temperature_count, expected_temperature_count)
        self.assertEqual(timestamp, expected_timestamp)


    def tearDown(self):
        """
        Delete the temporary json file
        """
        import os
        os.remove("test_data.json")

if __name__ == '__main__':
    unittest.main()