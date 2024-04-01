import json
import numpy as np

# Open and read json file
def read_json(sensorData):
    with open(sensorData, 'r') as file:
        data = json.load(file)
        return data

# Sort temperature and humidity
def processData(data):
    sortedData = sorted(data, key = lambda x: x['timestamp'])
    timestamp = [entry['timestamp'] for entry in sortedData]

    # Get data values in aray
    temperature = np.array([entry['temperature'] for entry in sortedData])
    humidity = np.array([entry]['humidity'] for entry in sortedData)
    
    # Round data values
    temperature = np.round(temperature).astype(int)
    humidity = np.round(humidity).astype(int)

    # Count the number of data points
    temperatureCount = {}
    humidityCount = {}

    for temp in temperature:
        if temp in temperatureCount:
            temperatureCount[temp] += 1
        else:
            temperatureCount[temp] = 1

    for humid in humidity:
        if humid in humidityCount:
            humidityCount[humid] += 1
        else:
            humidityCount[humid] = 1
    return humid, humidity, humidityCount, temp, temperature, temperatureCount, timestamp
