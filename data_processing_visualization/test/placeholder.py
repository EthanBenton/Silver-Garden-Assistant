import unittest
import numpy as np

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit_conversion(self):
        # Input temperatures in Celsius
        celsius_temperatures = np.array([0, 10, 20, 30, 40])
        
        # Expected output temperatures in Fahrenheit
        expected_fahrenheit_temperatures = np.array([32, 50, 68, 86, 104])
        
        # Convert Celsius temperatures to Fahrenheit
        fahrenheit_temperatures = (celsius_temperatures * 9/5) + 32
        
        # Check if the conversion is correct
        np.testing.assert_array_equal(fahrenheit_temperatures, expected_fahrenheit_temperatures, "Conversion from Celsius to Fahrenheit failed")

if __name__ == '__main__':
    unittest.main()