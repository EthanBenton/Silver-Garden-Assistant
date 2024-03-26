# constants.py
CONSTRAINTS = {
    'num_samples': (1, 10000),
    'temperature': (10, 30),
    'humidity': (30, 70),
    'polling_rate_seconds': (1, None),  # None means no upper bound
    'noise': (0, 10)
}

def validate_params(params):
    errors = {}

    for param, (lower, upper) in CONSTRAINTS.items():
        value = params.get(param)

        if value is None:
            continue

        if param == 'temperature':
            temp_start, temp_end = value
            if temp_start < lower or temp_end > upper or temp_start >= temp_end:
                errors[param] = f'Temperature range must be between {lower} and {upper} degrees Celsius, and temp_start must be less than temp_end'
        elif param == 'humidity':
            humidity_start, humidity_end = value
            if humidity_start < lower or humidity_end > upper or humidity_start >= humidity_end:
                errors[param] = f'Humidity range must be between {lower} and {upper} percent, and humidity_start must be less than humidity_end'
        else:
            lower_bound = lower if lower is not None else '-infinity'
            upper_bound = upper if upper is not None else 'infinity'
            if value < lower or (upper is not None and value > upper):
                errors[param] = f'{param.capitalize()} must be between {lower_bound} and {upper_bound}'

    return errors