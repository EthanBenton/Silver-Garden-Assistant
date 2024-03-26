import json
import numpy as np

# Read data from JSON file
def read_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Process data: sort and round temperature and humidity using numpy
def process_data(data):
    temperatures = np.array([entry['temperature'] for entry in data])
    humidities = np.array([entry['humidity'] for entry in data])

    temperatures = np.round(temperatures).astype(int)
    humidities = np.round(humidities).astype(int)

    temperature_counts = {}
    humidity_counts = {}

    for temp in temperatures:
        if temp in temperature_counts:
            temperature_counts[temp] += 1
        else:
            temperature_counts[temp] = 1

    for humidity in humidities:
        if humidity in humidity_counts:
            humidity_counts[humidity] += 1
        else:
            humidity_counts[humidity] = 1

    return temperature_counts, humidity_counts

# Generate HTML file with sorted and rounded data in separate columns
def generate_html(temperature_counts, humidity_counts, output_filename='datasort.html'):
    with open(output_filename, 'w') as file:
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>Sorted and Rounded Data</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1>Sorted and Rounded Data</h1>\n')
        
        file.write('<h2>Temperature</h2>\n')
        file.write('<table>\n')
        file.write('<tr><th>Temperature</th><th>Count</th></tr>\n')
        for temp, count in temperature_counts.items():
            file.write(f'<tr><td>{temp}</td><td>{count}</td></tr>\n')
        file.write('</table>\n')

        file.write('<h2>Humidity</h2>\n')
        file.write('<table>\n')
        file.write('<tr><th>Humidity</th><th>Count</th></tr>\n')
        for humidity, count in humidity_counts.items():
            file.write(f'<tr><td>{humidity}</td><td>{count}</td></tr>\n')
        file.write('</table>\n')

        file.write('</body>\n')
        file.write('</html>\n')

if __name__ == '__main__':
    input_filename = 'data_input_sim\src\sensor_data.json'
<<<<<<< HEAD
    output_filename = 'datasort.html'
=======
    output_filename = 'output.html'
>>>>>>> origin/main

    # Read data from JSON file
    data = read_data(input_filename)

    # Process data
    temperature_counts, humidity_counts = process_data(data)

    # Generate HTML file with sorted and rounded data in separate columns
    generate_html(temperature_counts, humidity_counts, output_filename)

    print(f'HTML file "{output_filename}" has been generated.')
