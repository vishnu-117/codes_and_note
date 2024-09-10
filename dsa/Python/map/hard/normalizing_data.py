measurements = [
    {'temperature_c': 0, 'temperature_f': None},
    {'temperature_c': 100, 'temperature_f': None},
    {'temperature_c': 37, 'temperature_f': None}
]

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(temp_c):
    return temp_c * 9/5 + 32

# Define a function that normalizes temperature in the dictionary
def normalize_measurement(measurement):
    measurement['temperature_f'] = celsius_to_fahrenheit(measurement['temperature_c'])
    return measurement

# Use map to apply the normalization function to each dictionary
normalized_measurements = list(map(normalize_measurement, measurements))

print(normalized_measurements)
# Output: [{'temperature_c': 0, 'temperature_f': 32.0}, {'temperature_c': 100, 'temperature_f': 212.0}, {'temperature_c': 37, 'temperature_f': 98.60000000000001}]
