import numpy as np
import random
from datetime import datetime, timedelta
import json

class SensorDataSimulator:
    """
    This class simulates the generation of temperature and humidity data with gradual changes.
    """

    def __init__(self, temperature_range=(0, 50), humidity_range=(0, 100), polling_rate_seconds=0, noise_mean=0.0, noise_std=0.0):
        """
        Initializes the simulator with defined ranges and change rate.

        Parameters:
        temperature_range (tuple): The range of possible temperatures.
        humidity_range (tuple): The range of possible humidities.
        noise_mean (float): The mean of the Gaussian noise added to the data.
        noise_std (float): The standard deviation of the Gaussian noise added to the data.
        """
        self.temperature_range = temperature_range
        self.humidity_range = humidity_range
        self.polling_rate = polling_rate_seconds
        self.start_timestamp = datetime.now()
        self.noise_mean = noise_mean
        self.noise_std  = noise_std
        self.previous_temperature = np.random.uniform(temperature_range[0], temperature_range[1])
        self.previous_humidity = np.random.uniform(humidity_range[0], humidity_range[1])
        

    def generate_data(self, num_samples, polling_rate_seconds):
        """
        Generates a list of dictionaries containing temperature and humidity data.

        Parameters:
        num_samples (int): The number of data samples to generate.
        polling_rate_seconds(int): number of seconds in-between data generation

        Returns:
        list: A list of dictionaries, each containing a temperature and humidity value.
        """
        temperatures = np.zeros(num_samples)
        humidities = np.zeros(num_samples)

        temperatures[0] = self.previous_temperature
        humidities[0] = self.previous_humidity

        data = []

        start_timestamp = datetime.now()

        for i in range(num_samples):
            timestamp = (start_timestamp + timedelta(seconds=i*polling_rate_seconds)).strftime("%Y-%m-%d %H:%M:%S")
            temperatures[i] = self._generate_temperature(temperatures[i-1])
            humidities[i] = self._generate_humidity(humidities[i-1])

            data_point = {'timestamp': timestamp, 'temperature': temperatures[i], 'humidity': humidities[i]}
            data.append(data_point)

        return data

    def _generate_temperature(self, previous_temperature):
        """
        Generates a temperature value within the range, including noise.

        Parameters:
        previous_temperature (float): The previous temperature value.

        Returns:
        float: The generated temperature value.
        """
        noisy_temperature = self._generate_noise(previous_temperature, self.temperature_range)

        self.previous_temperature = noisy_temperature

        return noisy_temperature

    def _generate_humidity(self, previous_humidity):
        """
        Generates a humidity value within the range, including noise.

        Parameters:
        previous_humidity (float): The previous humidity value.

        Returns:
        float: The generated humidity value.
        """
        noisy_humidity = self._generate_noise(previous_humidity, self.humidity_range)
        
        self.previous_humidity = noisy_humidity
    
        return noisy_humidity
    
    def _generate_noise(self, previous_value, value_range):
        """
        Generates noise for the given data value.

        Parameters:
        previous_value (float): The previous data value.
        value_range (tuple): The range of possible values.

        Returns:
        float: The data value with added noise.
        """
        
        noise = random.gauss(self.noise_mean, self.noise_std)  
        noisy_value = previous_value + noise
        noisy_value = max(value_range[0], min(noisy_value, value_range[1]))

        return noisy_value
    

    def write_to_json(self, data, filename):
        """
        Writes data to a JSON file.

        Parameters:
        data (list): The data to write to the file. This should be a list of dictionaries.
        filename (str): The name of the file to write to.
        """
        with open(filename, 'w') as f:
            json.dump(data, f)


if __name__ == "__main__":
    simulator = SensorDataSimulator(temperature_range=(20, 25), humidity_range=(50, 60), noise_mean=0.0, noise_std=0.5)
    data = simulator.generate_data(360, 10)
    simulator.write_to_json(data, 'sensor_data.json')

    for point in data[:50]:
       print(f"Timestamp {point['timestamp']}, Temperature: {point['temperature']:.2f} °C, Humidity: {point['humidity']:.2f} %")
