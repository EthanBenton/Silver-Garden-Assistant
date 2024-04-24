import unittest
import json
import pandas as pd

class TestDataNormalization(unittest.TestCase):
    def setUp(self):
        # Set up the file path for the test data
        self.input_file = 'data_processing_visualization\src\simulated_data_5.json'
        self.output_file = self.input_file  # Output the cleaned data back to the same file

        # Creates a sample JSON data
        self.sample_json_data = [
            {'timestamp': '2024-04-15T12:00:00Z', 'temperature': 20.5481, 'humidity': 45.4281},
            {'timestamp': '2024-04-15T13:00:00Z', 'temperature': 21.1472, 'humidity': 50.7594},
            {'timestamp': '2024-04-15T14:00:00Z', 'temperature': 19.9125, 'humidity': 44.8234},
        ]
        
        # Converts the sample data to JSON file
        with open('simulated_data_5.json', 'w') as file:
            json.dump(self.sample_json_data, file)
        
        # Loads the JSON data from the file
        with open('simulated_data_5.json', 'r') as file:
            self.sensor_data = json.load(file)
        
        # Create a DataFrame from the sensor data
        self.dataframe = pd.DataFrame(self.sensor_data)
        
    def test_normalization(self):
        # Round the temperature and humidity values
        self.dataframe['temperature'] = self.dataframe['temperature'].round(decimals=2)
        self.dataframe['humidity'] = self.dataframe['humidity'].round(decimals=2)
        
        # Convert the DataFrame back to a list of dictionaries
        cleaned_sensor_data = self.dataframe.to_dict(orient='records')
        
        # Check if the rounding is done correctly
        self.assertEqual(cleaned_sensor_data[0]['temperature'], 20.55)
        self.assertEqual(cleaned_sensor_data[0]['humidity'], 45.43)
        self.assertEqual(cleaned_sensor_data[1]['temperature'], 21.15)
        self.assertEqual(cleaned_sensor_data[1]['humidity'], 50.76)
        self.assertEqual(cleaned_sensor_data[2]['temperature'], 19.91)
        self.assertEqual(cleaned_sensor_data[2]['humidity'], 44.82)
        
    def tearDown(self):
        # Cleans up the test file
        import os
        os.remove('simulated_data_5.json')

if __name__ == '__main__':
    unittest.main()


        


