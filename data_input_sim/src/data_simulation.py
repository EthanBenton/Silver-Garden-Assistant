import numpy as np
from datetime import datetime, timedelta
import json
 
class SensorDataSimulator:
    """
    This class simulates the generation of temperature and humidity data with gradual changes.
    """

    def __init__(self, temperature_range=(0, 50), humidity_range=(0, 100), polling_rate_seconds=0, noise_mean=0.0, noise_std=0.0, temperature_variation=5):
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
        self.temperature_variation = temperature_variation
        
        

    def generate_data(self, num_samples, polling_rate_seconds):
        """
        Generates a list of dictionaries containing temperature and humidity data.

        Parameters:
        num_samples (int): The number of data samples to generate.
        polling_rate_seconds(int): number of seconds in-between data generation

        Returns:
        list: A list of dictionaries, each containing a temperature and humidity value.
        """
        self.num_samples = num_samples

        if num_samples <= 0:
            return []

        temperatures = np.zeros(num_samples)
        humidities = np.zeros(num_samples)

        temperatures[0] = self.previous_temperature
        humidities[0] = self.previous_humidity

        data = []

        start_timestamp = datetime.now()

        for i in range(num_samples):
            timestamp = start_timestamp + timedelta(seconds=i * polling_rate_seconds)
            temperatures[i] = self._generate_temperature(timestamp)
            humidities[i] = self._generate_humidity(humidities[i-1])

            data_point = {'humidity': humidities[i], 'temperature': temperatures[i],  'timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S")}
            data.append(data_point)

        return data

    def _generate_temperature(self, timestamp):
        """
        Generates a temperature value within the range, including realistic variations.
        # Formulae refactor + additional logic aided by Claude 

        Parameters:
        timestamp (datetime): The current timestamp.

        Returns:
        float: The generated temperature value.
        """
        hours = timestamp.hour + timestamp.minute / 60

        if 6 <= hours < 12:
            offset = (hours - 6) / 6 * self.temperature_variation * 0.6
        elif 12 <= hours < 18:
            offset = (18 - hours) / 6 * self.temperature_variation * 0.6
        else:
            offset = -self.temperature_variation * 0.4

        total_duration = (self.num_samples - 1) * self.polling_rate
        rate_of_change = (self.temperature_range[1] - self.temperature_range[0]) / total_duration
        elapsed_time = (timestamp - self.start_timestamp).total_seconds()

     
        new_temperature = self.temperature_range[0] + rate_of_change * elapsed_time + offset
        noise = np.random.normal(self.noise_mean, self.noise_std)
        new_temperature += noise


        buffer = self.temperature_variation * 0.2
        min_temp = self.temperature_range[0] + buffer
        max_temp = self.temperature_range[1] - buffer
        new_temperature = max(min_temp, min(new_temperature, max_temp))

        return new_temperature
                
    def _generate_humidity(self, previous_humidity):
        """
        Generates a humidity value within the range, including noise.

        Parameters:
        previous_humidity (float): The previous humidity value.

        Returns:
        float: The generated humidity value.
        """
        
        humidity_change = np.random.normal(0, 1)

        
        new_humidity = previous_humidity + humidity_change

        
        new_humidity = max(self.humidity_range[0], min(new_humidity, self.humidity_range[1]))

        self.previous_humidity = new_humidity
        return new_humidity
        

    def write_to_json(self, data, filename):
        """
        Writes data to a JSON file.

        Parameters:
        data (list): The data to write to the file. This should be a list of dictionaries.
        filename (str): The name of the file to write to.
        """
        with open(filename, 'w') as f:
            json.dump(data, f, indent = 4)
            
if __name__ == "__main__":
    simulator = SensorDataSimulator(temperature_range=(20, 25), humidity_range=(50, 60), noise_mean=0.0, noise_std=0.5)
    data = simulator.generate_data(360, 10)
    simulator.write_to_json(data, 'sensor_data.json')

    for point in data[:50]:
       print(f"Timestamp {point['timestamp']}, Temperature: {point['temperature']:.2f} °C, Humidity: {point['humidity']:.2f} %")
