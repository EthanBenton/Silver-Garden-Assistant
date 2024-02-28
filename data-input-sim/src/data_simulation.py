import random

class SensorDataSimulator:
    """
    Simulates temperature and humidity data me with gradual changes.
    """

    def __init__(self, temperature_range=(15, 30), humidity_range=(40, 60), change_rate=0.1):
        """
        Initializes the simulator with defined ranges and change rate.
        """
        self.temperature_range = temperature_range
        self.humidity_range = humidity_range
        self.change_rate = change_rate
        self.previous_temperature = None
        self.previous_humidity = None

    def generate_data(self, num_samples):
        """
        Generates a list of dictionaries containing temperature and humidity data.
        """
        data = []
        for _ in range(num_samples):
            temperature = self._generate_temperature()
            humidity = self._generate_humidity()
            data.append({'temperature': temperature, 'humidity': humidity})
        return data

    def _generate_temperature(self):
        """
        Generates a temperature value within the range.
        """
        if self.previous_temperature is None:
            self.previous_temperature = random.uniform(self.temperature_range[0], self.temperature_range[1])

        change = random.uniform(-self.change_rate, self.change_rate)

        new_temperature = max(self.temperature_range[0], min(self.temperature_range[1], self.previous_temperature + change))

        self.previous_temperature = new_temperature
        
        return new_temperature

    def _generate_humidity(self):
        """
        Generates a humidity value within the range.
        """
        if self.previous_humidity is None:
            self.previous_humidity = random.uniform(self.humidity_range[0], self.humidity_range[1])

        change = random.uniform(-self.change_rate, self.change_rate)

        new_humidity = max(self.humidity_range[0], min(self.humidity_range[1], self.previous_humidity + change))

        self.previous_humidity = new_humidity

        return new_humidity


if __name__ == "__main__":
    simulator = SensorDataSimulator(temperature_range=(20, 25), humidity_range=(50, 60), change_rate=0.05)
    data = simulator.generate_data(100)

    for point in data[:50]:
        print(f"Temperature: {point['temperature']:.2f} °C, Humidity: {point['humidity']:.2f} %")
