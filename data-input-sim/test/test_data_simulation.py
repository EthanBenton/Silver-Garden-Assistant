# test_data_simulation.py
from src.data_simulation import SensorDataSimulator
import pytest

@pytest.fixture
def simulator():
    """
    Fixture to create a SensorDataSimulator object for testing.
    """
    return SensorDataSimulator(temperature_range=(20, 25), humidity_range=(40, 60))

def test_temperature_within_range(simulator):
    """
    Tests if temperature stays within the range.
    """
    new_temp = simulator._generate_temperature()

    assert 20 <= new_temp <= 25  

def test_humidity_within_range(simulator):
    """
    Tests if humidity stays within the range.
    """
    new_temp = simulator._generate_humidity()

    assert 40 <= new_temp <= 60  