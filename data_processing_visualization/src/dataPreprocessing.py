import json

with open('data_processing_visualization\\src\\simulated_data_5.json' , 'r') as raw_file:
    raw_data = json.load(raw_file)


    aggregated_temps = [entry['temperature'] for entry in raw_data]

    aggregated_humid  = [entry['humidity'] for entry in raw_data]
    aggregated_time = [entry['timestamp'] for entry in raw_data]


    temperature = []
    humidity = []
    timestamps = []

    for i in range(0, len(aggregated_time), 5):
        temp_summation = sum(aggregated_temps[i:i+5])
        humid_summation = sum(aggregated_humid[i:i+5])

        avg_timestamp = aggregated_time[i]

        avg_temperature = temp_summation / 5  # Calculate average temperature
        avg_humidity = humid_summation / 5     # Calculate average humidity

        temperature.append(avg_temperature)
        humidity.append(avg_humidity)
        timestamps.append(avg_timestamp)

    new_aggregated_data = {
        "humidity": humidity,
        "temperatures": temperature,
        "timestamps": timestamps
    }

    # Export new aggregated data to JSON
    with open('data_processing_visualization//src//simulated_data_5.json', 'w') as new_file:
        json.dump(new_aggregated_data, new_file, indent=4)

    print("Aggregated data exported to 'data_processing_visualization//src//simulated_data_5.json'.")
