import json

flight={'flight_number':'1700','airline':'Indigo','capacity':180,'price':5000}
file_name='flight.json'

print(flight)
with open(file_name,'w') as writer:
    json.dump(flight,writer)
    print("saved the flight to file")

with open(file_name,'r') as reader:
    flight_from_file=json.load(reader)
    print(flight_from_file)