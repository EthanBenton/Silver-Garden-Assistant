
from flask import Flask, request, session, jsonify
from data_input_sim import validate_params
from data_input_sim import SensorDataSimulator

app = Flask(__name__, static_folder='src/flask/static')
app.secret_key = 'your_secret_key'  # Set a secret key for session encryption

@app.route('/api/simulate', methods=['POST'])
def simulate():
    params = request.get_json()

    errors = validate_params(params)
    if errors:
        return jsonify(errors), 400

    # Proceed with simulation if no errors
    num_samples = params.get('num_samples')
    temperature = params.get('temperature')
    humidity = params.get('humidity')
    polling_rate_seconds = params.get('polling_rate_seconds')
    noise_mean = params.get('noise_mean')
    noise_std = params.get('noise_std')

    # Check if required parameters are present and are not None
    if num_samples is None or temperature is None or humidity is None or polling_rate_seconds is None or noise_mean is None or noise_std is None:
        return jsonify(error='Required parameters are missing or invalid'), 400

    # Unpack temperature and humidity values
    temp_start, temp_end = temperature
    humidity_start, humidity_end = humidity

    simulator = SensorDataSimulator((temp_start, temp_end), (humidity_start, humidity_end), polling_rate_seconds, noise_mean, noise_std)
    data = simulator.generate_data(num_samples, polling_rate_seconds)

    # Return the data as a JSON response
    return jsonify(data)

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error
    app.logger.error(str(e))
    # Return an error response
    return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)