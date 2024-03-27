from flask import Flask, request, jsonify

from data_input_sim import validate_params
from data_input_sim import SensorDataSimulator

app = Flask(__name__, static_folder='src/flask/static')
app.secret_key = 'your_secret_key'  


simulator = None

@app.route('/api/simulate', methods=['POST'])
def simulate():
    global simulator
    params = request.get_json()
    print("Received payload:", params)

    errors = validate_params(params)
    if errors:
        print(errors)
        return jsonify(errors), 400


    num_samples = params.get('num_samples')
    temp_start = float(params.get('temp_start'))
    temp_end = float(params.get('temp_end'))
    humidity_start = float(params.get('humidity_start'))
    humidity_end = float(params.get('humidity_end'))
    polling_rate_seconds = params.get('polling_rate_seconds')
    noise_mean = float(params.get('noise_mean'))
    noise_std = float(params.get('noise_std'))


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

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)