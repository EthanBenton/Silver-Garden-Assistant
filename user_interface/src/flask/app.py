import sys
import os
import logging
import os.path
import json 

from flask import Flask, request, jsonify
from flask import current_app

#needed for flask to use the other files
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, project_root)

from data_input_sim.src.constraint_validation import validate_params
from data_input_sim.src.data_simulation import SensorDataSimulator
from data_processing_visualization.src.graphing_tool import graphingTool


"""
    Initialize flask app
"""
app = Flask(__name__, static_folder='static')

"""
    Setting up basic configuration for logging
""" 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

    
@app.route('/api/graph0', methods=['POST'])
def graph0():
    """
    API endpoint to generate a graph from simulated data using UI interaction and for an interactive graph located at GrapsPage0.js.
    """
    try:
        simulated_data = request.get_json()
        if not simulated_data:
            return jsonify({"error": "No simulated data received"}), 400

        data_dir = os.path.join(current_app.static_folder, 'data')

        os.makedirs(data_dir, exist_ok=True)

        json_file_path = os.path.join(data_dir, 'simulated_data.json')

        with open(json_file_path, 'w') as f:
            json.dump(simulated_data, f, indent = 4)

        graph = graphingTool(json_file_path)
        export_name = 'simulated_data'
        graph.set_export_name(export_name)
        graph.indexed_json_to_html(2, 1, 0, "Simulated Data Visualization")

        return jsonify({"message": "Graph generated successfully", "filePath": f"/static/data/{export_name}.html"})
    except Exception as e:
        logger.error(f"Failed to generate graph: {e}")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global exception handler for the Flask app.
    """
    logger.error(f"Unhandled exception: {e}")
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)