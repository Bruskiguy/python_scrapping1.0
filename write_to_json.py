import json

# Converts to JSON and writes to data.json


def write_to_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)
