from random import randrange
import time
from utils.parse_one import bs4_get_search_results
from utils.write_to_json import write_to_json
import csv

keywords = []

with open('keywords.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for key, value in row.items():
            keywords.append(value)

file_path = "data.json"

# Keywords run through parse_one.py, where the Pages HTML is fetched and parsed, and outputs the data all at once to data.json (should be optimized later?)
for i in range(len(keywords)):
    tag = keywords[i]

    # every 100'th keyword we create a new file eg. `data100.json`
    if i and i % 50 == 0:
        file_path = f"data{i}.json"

    result = bs4_get_search_results(tag)

    while (not result or not len(result)):
        print(f"WARNING - {tag} - returned an empty result")
        user_input = input(
            "You should change IP with VPN, Do you want to continue? (y/n)")
        if user_input == "n":
            break

    print(tag)
    write_to_json({tag: result}, file_path)
    # the ultimate secret to not being caught by google.
    time.sleep(randrange(3, 7))
