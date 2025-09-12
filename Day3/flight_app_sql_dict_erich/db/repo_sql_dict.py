from .db_setup import session, Flight
from .log import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import FlightAlreadyExistError, DatabaseError, FlightNotFoundError

# CRUD (Create, Read All | Read One, Update, Delete)
# Flight App - SQL DB - dict element

def create_flight(flight):
    try:
        flight_model = Flight(
            id=flight['id'],
            airline=flight['airline'],
            origin=flight['origin'],
            destination=flight['destination'],
            price=flight['price'],
            is_active=flight['is_active']
        )
        session.add(flight_model)
        session.commit()
        logging.info("flight created successfully")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate flight id: %s", ex)
        raise FlightAlreadyExistError(f"flight id={flight['id']} exists already")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("database Error occurred while creating flight: %s", ex)
        raise DatabaseError("error occurred in creating flight")

def read_all_flights():
    flights = session.query(Flight).all()
    dict_flights = []
    for flight in flights:
        flight_dict = {
            'id': flight.id,
            'airline': flight.airline,
            'origin': flight.origin,
            'destination': flight.destination,
            'price': flight.price,
            'is_active': flight.is_active
        }
        dict_flights.append(flight_dict)
    logging.info("read all flights.")
    return dict_flights

def read_model_by_id(id):
    flight = session.query(Flight).filter(Flight.id == id).first()
    logging.info("read flight model.")
    return flight

def read_by_id(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight with id={id} not found")
        return None
    flight_dict = {
        'id': flight.id,
        'airline': flight.airline,
        'origin': flight.origin,
        'destination': flight.destination,
        'price': flight.price,
        'is_active': flight.is_active
    }
    logging.info("read flight for given id.")
    return flight_dict

def update(id, new_flight):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight with id={id} not found")
        return None
    flight.price = new_flight['price']
    session.commit()
    logging.info(f"flight with id={id} updated successfully")
    return new_flight

def delete_flight(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight not found {id}.")
        return None
    session.delete(flight)
    session.commit()
    logging.info(f"flight with id={id} deleted successfully")