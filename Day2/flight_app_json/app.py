import repo_json_dict as repo

def menu():
    message = '''
Options are:
1 - Create Flight
2 - List All Flights
3 - Read Flight By Id
4 - Update Flight
5 - Delete Flight
6 - Exit 
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        number = input('Flight Number:')
        airline_name = input('Airline Name:')
        seats = int(input('Seats:'))
        price = float(input('Price:'))
        source = input('Source:')
        destination = input('Destination:')
        flight = {'id':id, 'number':number, 'airline_name':airline_name,
                  'seats':seats, 'price':price, 'source':source, 'destination':destination}
        repo.create_flight(flight)
        print('Flight Created Successfully.')
    elif choice == 2:
        print('List of Flights:')
        for flight in repo.read_all_flights():
            print(flight)
    elif choice == 3:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight is None:
            print('Flight not found.')
        else:
            print(flight)
    elif choice == 4:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight is None:
            print('Flight Not Found')
        else:
            print(flight)
            price = float(input('New Price:'))
            new_flight = {**flight, 'price': price}
            repo.update(id, new_flight)
            print('Flight updated successfully.')
    elif choice == 5:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight is None:
            print('Flight Not Found')
        else:
            repo.delete_flight(id)
            print('Flight Deleted Successfully.')
    elif choice == 6:
        print('Thank you for using Application')
    return choice

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()

menus()