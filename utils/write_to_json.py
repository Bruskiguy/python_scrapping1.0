import json
import os

file_path = "data.json"


def write_to_json(data):
    # check if exists
    if os.path.isfile("data.json"):
        print("exists")
        with open('data.json', "r+") as f:
            prev_data = json.load(f)
            s = prev_data
            # data comes as [{"first_item":[...tags+titles]}]
            # we don't need the wrapping array
            s.update(data[0])
            # move cursor to beginning - bc we want to paste the new values on top
            f.seek(0)
            json.dump(s, f)
    else:
        with open('data.json', "w+") as f:
            json.dump(data[0], f)
