import unittest
import json
import pandas as pd
from datetime import datetime
import sys
sys.path.append('data_processing_visualization/src/')
from WateringSchedule import WateringSchedule

class TestWaterSchedule(unittest.TestCase):

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

    def test_load_sensor_data(self):
        """
        Test the load_sensor_data method
        """
        watering_schedule = WateringSchedule()
        data = watering_schedule.load_sensor_data("test_data.json")
        self.assertEqual(data, self.test_data)

    def test_create_dataframe(self):
        """
        Test the create_dataframe method
        """
        watering_schedule = WateringSchedule()
        df_expected = pd.DataFrame({
            'humidity': [46.11708606933448, 54.59773018104158],
            'temperature': [24.463786814431522, 26.059561397324842],
            'timestamp': [datetime.strptime("2024-04-11 20:56:49", '%Y-%m-%d %H:%M:%S'), datetime.strptime("2024-04-11 20:57:49", '%Y-%m-%d %H:%M:%S')]
        })
        df_expected.set_index('timestamp', inplace=True)
        df_expected = df_expected.resample('1h').mean().interpolate()

        data = watering_schedule.create_dataframe(self.test_data)
        pd.testing.assert_frame_equal(data, df_expected)

        def test_create_watering_schedule(self):
            """
            Test the create_watering_schedule method
            """
            watering_schedule = WateringSchedule()
            df = pd.DataFrame({
                'humidity': [50, 60, 40, 70],
                'temperature': [24, 26, 27, 23],
                'timestamp': [datetime(2024, 4, 11, 8), datetime(2024, 4, 11, 9), datetime(2024, 4, 11, 10), datetime(2024, 4, 11, 11)]
            })
            df.set_index('timestamp', inplace=True)

            expected_df = pd.DataFrame({
                'humidity': [50, 60, 40, 70],
                'temperature': [24, 26, 27, 23],
                'watering_schedule': [0, 1, 1, 0],
                'days_of_the_week': ['Monday', 'Monday', 'Monday', 'Monday']
            })
            expected_df.set_index('timestamp', inplace=True)

            result_df = watering_schedule.create_watering_schedule(df)
            pd.testing.assert_frame_equal(result_df, expected_df)

        def tearDown(self):
            """
            Delete the temporary json file
            """
            import os
            os.remove("test_data.json")

if __name__ == '__main__':
    unittest.main()