from db import repo_sql_dict as repo

def menu():
    message = '''
Options are:
1 - Create Flight
2 - List All Flights
3 - Read Flight By Id
4 - Update Flight Price
5 - Delete Flight
6 - Exit 
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        airline = input('Airline:')
        origin = input('Origin:')
        destination = input('Destination:')
        price = float(input('Price:'))
        is_active = (input('Active(y/n):').upper() == 'Y')

        flight = {
            'id': id,
            'airline': airline,
            'origin': origin,
            'destination': destination,
            'price': price,
            'is_active': is_active
        }
        try:
            repo.create_flight(flight)
            print('Flight Created Successfully.')
        except repo.FlightAlreadyExistError as ex:
            print(f"{ex}")
        except repo.DatabaseError as ex:
            print(f"{ex}")

    elif choice == 2:
        print('List of Flights:')
        for flight in repo.read_all_flights():
            print(flight)
    elif choice == 3:
        id = int(input('ID:'))
        try:
            flight = repo.read_by_id(id)
            print(flight)
        except repo.FlightNotFoundError as ex:
            print(f"{ex}")
    elif choice == 4:
        id = int(input('ID:'))
        try:
            flight = repo.read_by_id(id)
            print(flight)
            price = float(input('New Price:'))
            new_flight = {**flight, 'price': price}
            repo.update(id, new_flight)
            print('Flight updated successfully.')
        except repo.FlightNotFoundError as ex:
            print(f"{ex}")
    elif choice == 5:
        id = int(input('ID:'))
        try:
            repo.delete_flight(id)
            print('Flight Deleted Successfully.')
        except repo.FlightNotFoundError as ex:
            print(f"{ex}")
    elif choice == 6:
        print('Thank you for using Application')

    return choice

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()

menus()