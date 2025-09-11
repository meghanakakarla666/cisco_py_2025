import pickle
import os

def read_from_file(filename='flights.dat'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'rb') as reader:
        return pickle.load(reader)

def write_to_file(flights, filename='flights.dat'):
    with open(filename, 'wb') as writer:
        pickle.dump(flights, writer)