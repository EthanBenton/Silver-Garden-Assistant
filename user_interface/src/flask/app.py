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

def UI_button_interaction():
    """
    Event script that runs upon a button press.
    It targets a single json file for the initially generated data.
    """
    json_file_path = "user_interface/src/frontend/public/graphs/sensor_data.json"
    export_name = json_file_path.split('/')[-1].split(".json")[0]  # Extracts 'sensor_data' from the file path

    graph = graphingTool(json_file_path)
    graph.set_export_name(export_name)
    graph.indexed_json_to_html(index=2, indey=1, indey2=0, title=export_name)

    return export_name  # Return the base name for use in the endpoint

@app.route('/api/graph0', methods=['POST'])
def graph0():
    try:
        export_name = UI_button_interaction()
        return jsonify({"message": "Graph generated successfully", "filePath": f"/graphs/{export_name}.html"})
    except Exception as e:
        app.logger.error(f"Failed to generate graph: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)