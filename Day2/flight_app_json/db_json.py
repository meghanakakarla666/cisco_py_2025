import json
import os

def read_from_file(filename='flights.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as reader:
        return json.load(reader)

def write_to_file(flights, filename='flights.json'):
    with open(filename, 'w') as writer:
        json.dump(flights, writer)