import json
import numpy as np

# Open and read json file
def read_data(sensorData):
    with open(sensorData, 'r') as file:
        data = json.load(file)
        return data

# Sort temperature and humidity
def processData(data):
    sortedData = sorted(data, key = lambda x: x['timestamp'])
    timestamp = [entry['timestamp'] for entry in sortedData]

    # Get data values in aray
    temperature = np.array([entry['temperature'] for entry in sortedData])
    humidity = np.array([entry['humidity'] for entry in sortedData])
    
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
    return humidity, humidityCount, temperature, temperatureCount, timestamp

# Makes the html file with its table output
def makehtml(humidity, humidityCount, temperature, temperatureCount, timestamp, outputFile = 'Data.html'):
    with open(outputFile, 'w') as file:
        # Table formatting
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>Processed Data</title>\n')
        file.write('<style>\n')
        file.write('table {\n')
        file.write('    border-collapse: collapse;\n')
        file.write('    width: 50%;\n')
        file.write('}\n')
        file.write('th, td {\n')
        file.write('    border: 1px solid black;\n')
        file.write('    padding: 8px;\n')
        file.write('    text-align: center;\n')
        file.write('}\n')
        file.write('</style>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1>Processed Data</h1>\n')

        file.write('<div style="display:flex;">\n')
        file.write('<div style="flex:33%; height: 310px; overflow-y: auto; padding: 5px; margin-right: -5px; position-relative;\n">\n')
        file.write('<h2 style=" position:sticky; top: 0; background-color: white; z-index: 1"> Temperature</h2>\n')
        file.write('<table>\n')
        file.write('<tr><th>Temperature</th><th>Count</th></tr>\n')
        sorted_temperatures = sorted(temperatureCount.items(), key = lambda x: x[0])
        for temp, count in sorted_temperatures:
            file.write(f'<tr><td>{temp}</td><td>{count}</td></tr>\n')
        file.write('</table>\n')
        file.write(f'<p>Total Temperature Data Points: {sum(temperatureCount.values())}</p>\n')
        file.write('</div>\n')

        file.write('<div style="flex:33%; height: 310px; overflow-y: auto; padding: 5px; margin-right: -5px; position-relative;\n">\n')
        file.write('<h2 style=" position:sticky; top: 0; background-color: white; z-index: 1"> Humidity</h2>\n')
        file.write('<table>\n')
        file.write('<tr><th>Humidity</th><th>Count</th></tr>\n')
        sorted_humidities = sorted(humidityCount.items(), key = lambda x: x[0])
        for humid, count in sorted_humidities:
            file.write(f'<tr><td>{humid}</td><td>{count}</td></tr>\n')
        file.write('</table>\n')
        file.write(f'<p>Total Humidity Data Points: {sum(humidityCount.values())}</p>\n')
        file.write('</div>\n')

        file.write('<div style="flex:33%; height: 310px; overflow-y: auto; padding: 5px; margin-right: -5px; position-relative;\n">\n')
        file.write('<h2 style=" position:sticky; top: 0; background-color: white; z-index: 1"> All Data with Timestamps</h2>\n')
        file.write('<table>\n')
        file.write('<tr><th>Temperature</th><th>Humidity</th><th>Timestamp</th></tr>\n')
        for i in range(len(timestamp)):
            file.write(f'<tr><td>{temperature[i]}</td><td>{humidity[i]}</td><td>{timestamp[i]}</td></tr>\n')
        file.write('</table>\n')
        file.write('</div>\n')

        file.write('</div>\n')
        file.write('</body>\n')
        file.write('</html>\n')

if __name__ == '__main__':
    inputFile = 'user_interface\\src\\flask\\static\\data\\sensor_data.json'
    outputFile = 'user_interface\\src\\frontend\\public\\graphs\\DataTables.html'

    data = read_data(inputFile)

    temperature, temperatureCount, humidity, humidityCount, timestamp = processData(data)

    makehtml(humidity, humidityCount, temperature, temperatureCount, timestamp, outputFile)

    print(f'DataTables.html has been made')