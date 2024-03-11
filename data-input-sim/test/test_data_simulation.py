# test_data_simulation.py
from src.data_simulation import SensorDataSimulator
import pytest
import numpy as np


@pytest.fixture
def simulator():
    """
    Fixture to create a SensorDataSimulator object for testing.
    """
    return SensorDataSimulator(temperature_range=(20, 25), humidity_range=(40, 60), noise_mean= 0.0, noise_std= 0.5)


@pytest.fixture(params=[(20, 25), (15, 30)], ids=['normal_range', 'wide_range'])
def temperature_range(request):
    return request.param


@pytest.fixture(params=[(40, 60), (30, 70)], ids=['normal_range', 'wide_range'])
def humidity_range(request):
    return request.param


def test_temperature_within_range(simulator, temperature_range):
    """
    Tests if temperature stays within the range.
    """
    num_samples = 1000
    temperatures = [simulator.previous_temperature]

    for _ in range(num_samples - 1):
        temperatures.append(simulator._generate_temperature(temperatures[-1]))

    assert all(temperature_range[0] <= temp <= temperature_range[1] for temp in temperatures)


def test_humidity_within_range(simulator, humidity_range):
    """
    Tests if humidity stays within the range.
    """
    num_samples = 1000
    humidities = [simulator.previous_humidity]

    for _ in range(num_samples - 1):
        humidities.append(simulator._generate_humidity(humidities[-1]))

    assert all(humidity_range[0] <= hum <= humidity_range[1] for hum in humidities), "Generated humidity is out of range."

def test_noise_mean(simulator):
    """
    Tests if the noise generation for humidity and temperature has the expected mean.
    """
    # Generate noisy data
    num_samples = 1000
    noisy_humidities = np.array([simulator._generate_noise(simulator.previous_humidity, simulator.humidity_range) for _ in range(num_samples)])
    noisy_temperatures = np.array([simulator._generate_noise(simulator.previous_temperature, simulator.temperature_range) for _ in range(num_samples)])

    # Calculate mean
    calculated_humidity_mean = round(np.mean(noisy_humidities), 2)
    calculated_temperature_mean = round(np.mean(noisy_temperatures), 2)

    # Assert within tolerance
    tolerance = 0.1
    assert abs(calculated_humidity_mean - simulator.previous_humidity) < tolerance
    assert abs(calculated_temperature_mean - simulator.previous_temperature) < tolerance


def test_noise_std_dev(simulator):
    """
    Tests if the noise generation for humidity and temperature has the expected standard deviation.
    """
    # Generate noisy data
    num_samples = 1000
    noisy_humidities = np.array([simulator._generate_noise(simulator.previous_humidity, simulator.humidity_range) for _ in range(num_samples)])
    noisy_temperatures = np.array([simulator._generate_noise(simulator.previous_temperature, simulator.temperature_range) for _ in range(num_samples)])

    # Calculate standard deviation
    calculated_humidity_std_dev = round(np.std(noisy_humidities), 2)
    calculated_temperature_std_dev = round(np.std(noisy_temperatures), 2)

    # Assert within tolerance
    tolerance = 0.1
    assert abs(calculated_humidity_std_dev - simulator.noise_std) < tolerance
    assert abs(calculated_temperature_std_dev - simulator.noise_std) < tolerance
