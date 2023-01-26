import json
import os


def write_to_json(data, file_path: str):
    # check if exists
    if os.path.isfile(file_path):
        with open('data.json', "r+") as f:
            prev_data = json.load(f)
            s = prev_data
            s.update(data)

            # move cursor to beginning - bc we want to paste the new values on top
            f.seek(0)
            json.dump(s, f)
    else:
        with open(file_path, "w+") as f:
            json.dump(data, f)
