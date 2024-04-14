from flask import Flask, request, jsonify, send_from_directory
import sys
import pandas as pd 
import os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, project_root)

from data_input_sim.src.constraint_validation import validate_params
from data_input_sim.src.data_simulation import SensorDataSimulator
from data_processing_visualization.src.graphing_tool import graphingTool

app = Flask(__name__, static_folder='src/flask/static')
app.secret_key = 'your_secret_key'  


simulator = None


def convert_to_seconds(time_interval, time_unit):
    time_units_in_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2592000,
    }
    return time_interval * time_units_in_seconds[time_unit]

def calculate_max_samples(time_interval_seconds, polling_rate_seconds):
    return int(time_interval_seconds // polling_rate_seconds)


@app.route('/api/simulate', methods=['POST'])
def simulate():
    global simulator
    params = request.get_json()
    print("Received payload:", params)
    


    time_unit = params.get('time_unit')
    time_interval = params.get('time_interval')
    print("time_unit:", time_unit)
    print("time_interval:", time_interval)


    errors = validate_params(params)
    if errors:
        print(errors)
        return jsonify(errors), 400


    temp_start = float(params.get('temp_start'))
    temp_end = float(params.get('temp_end'))
    humidity_start = float(params.get('humidity_start'))
    humidity_end = float(params.get('humidity_end'))
    polling_rate_seconds = (params.get('polling_rate_seconds'))
    noise_mean = float(params.get('noise_mean'))
    noise_std = float(params.get('noise_std'))
    time_unit = params.get('time_unit')
    time_interval = float(params.get('time_interval')) 


   
    total_seconds = convert_to_seconds(time_interval, time_unit)

    num_samples = calculate_max_samples(total_seconds, polling_rate_seconds)

    print("num_samples:", num_samples)
    print("temp_start:", temp_start)
    print("temp_end:", temp_end)
    print("humidity_start:", humidity_start)
    print("humidity_end:", humidity_end)
    print("polling_rate_seconds:", polling_rate_seconds)
    print("noise_mean:", noise_mean)
    print("noise_std:", noise_std)


    if None in (num_samples, temp_start, temp_end, humidity_start, humidity_end, polling_rate_seconds, noise_mean, noise_std):
        return jsonify(error='Required parameters are missing or invalid'), 400


    if simulator is None:
        simulator = SensorDataSimulator((temp_start, temp_end), (humidity_start, humidity_end), polling_rate_seconds, noise_mean, noise_std)

    data = simulator.generate_data(num_samples, polling_rate_seconds)

    return jsonify(data)

@app.route('/api/generate-graph', methods=['POST'])
def generate_graph():
    try:
        # Assuming the JSON file path is fixed or dynamically determined elsewhere
        data_file_path = 'data_input_sim/src/simulated_data.json'
        graph_tool = graphingTool(data_source=data_file_path)
        graph_tool.indexed_json_to_html(index=0, indey=1, indey2=-1, title="Your Graph Title")

        # Return the path or acknowledge that the graph was created
        return jsonify({"message": "Graph generated successfully", "filePath": "/graphs/Graph.html"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)