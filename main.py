from random import randrange
import time
from parse_one import bs4_get_search_results
from write_to_json import write_to_json
import csv

keywords = []
with open('keywords.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for key, value in row.items():
            keywords.append(value)

# Keywords run through parse_one.py, where the Pages HTML is fetched and parsed, and outputs the data all at once to data.json (should be optimized later?)
z = []

for tag in keywords[:20]:
    result = bs4_get_search_results(tag)
    print(tag)
    z.append({tag: result})
# the ultimate secret to not being caught by google.
    time.sleep(randrange(3, 7))

print(z)
write_to_json(z)
