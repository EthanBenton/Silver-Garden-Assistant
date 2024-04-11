import json

# Read data from JSON file
def read_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Generate HTML file with line graph based on timestamp, temperature, and humidity
def generate_html(data, output_filename='graph.html'):
    with open(output_filename, 'w') as file:
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>Temperature and Humidity Data</title>\n')
        file.write('<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n')  # Include Plotly library
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1>Temperature and Humidity Data</h1>\n')
        
        timestamps = [entry['timestamp'] for entry in data]
        temperatures = [entry['temperature'] for entry in data]
        humidities = [entry['humidity'] for entry in data]

        # Write JavaScript code to generate line graph
        file.write('<div id="chart"></div>\n')
        file.write('<script>\n')
        file.write('var trace1 = {\n')
        file.write('  x: ' + str(timestamps) + ',\n')
        file.write('  y: ' + str(temperatures) + ',\n')
        file.write("  mode: 'lines+markers',\n")
        file.write("  name: 'Temperature'\n")
        file.write('};\n')
        file.write('var trace2 = {\n')
        file.write('  x: ' + str(timestamps) + ',\n')
        file.write('  y: ' + str(humidities) + ',\n')
        file.write("  mode: 'lines+markers',\n")
        file.write("  name: 'Humidity'\n")
        file.write('};\n')
        file.write('var layout = {\n')
        file.write("  title: 'Temperature and Humidity Data',\n")
        file.write("  xaxis: {title: 'Timestamp'},\n")
        file.write("  yaxis: {title: 'Value'}\n")
        file.write('};\n')
        file.write('var data = [trace1, trace2];\n')
        file.write('Plotly.newPlot("chart", data, layout);\n')
        file.write('</script>\n')

        file.write('</body>\n')
        file.write('</html>\n')

if __name__ == '__main__':
    input_filename = 'new_sensor_data.json'
    output_filename = 'graph.html'

    # Read data from new_sensor_data.json file
    data = read_data(input_filename)

    # Generate a HTML file
    generate_html(data, output_filename)

    print(f'HTML file "{output_filename}" with line graph has been generated.')
