import json


def write_to_json(data):
    with open('data.json', "r") as f:
        data = json.load(f)
    data.append(data)
    with open('data.json', "w") as f:
        json.dump(data, f)
