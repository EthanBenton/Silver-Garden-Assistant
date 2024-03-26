
from flask import Flask, request, jsonify
from data_input_sim import validate_params
from data_input_sim import SensorDataSimulator

app = Flask(__name__, static_folder='src/flask/static')
app.secret_key = 'your_secret_key'  # Set a secret key for session encryption

@app.route('/api/simulate', methods=['POST'])
def simulate():
    params = request.get_json()

    errors = validate_params(params)
    if errors:
        print(errors)
        return jsonify(errors), 400

    # Proceed with simulation if no errors
    num_samples = params.get('num_samples')
    temp_start = params.get('temp_start')
    temp_end = params.get('temp_end')
    humidity_start = params.get('humidity_start')
    humidity_end = params.get('humidity_end')
    polling_rate_seconds = params.get('polling_rate_seconds')
    noise_mean = params.get('noise_mean')
    noise_std = params.get('noise_std')
    
    if num_samples is None or temp_start is None or temp_end is None or humidity_start is None or humidity_end is None or polling_rate_seconds is None or noise_mean is None or noise_std is None:
        return jsonify(error='Required parameters are missing or invalid'), 400

    simulator = SensorDataSimulator((temp_start, temp_end), (humidity_start, humidity_end), noise_mean, noise_std)
    data = simulator.generate_data(num_samples, polling_rate_seconds)

    return jsonify(data)

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)