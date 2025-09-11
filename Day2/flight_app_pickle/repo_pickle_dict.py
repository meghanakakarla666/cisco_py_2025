import db_pickle as db

file_name = 'flights.dat'
flights = db.read_from_file(file_name)

def create_flight(flight):
    global flights
    flights.append(flight)
    db.write_to_file(flights, file_name)

def read_all_flights():
    return flights

def read_by_id(id):
    for flight in flights:
        if flight['id'] == id:
            return flight
    return None

def update(id, new_flight):
    global flights
    for i, flight in enumerate(flights):
        if flight['id'] == id:
            flights[i] = new_flight
            db.write_to_file(flights, file_name)
            break

def delete_flight(id):
    global flights
    for i, flight in enumerate(flights):
        if flight['id'] == id:
            flights.pop(i)
            db.write_to_file(flights, file_name)
            break