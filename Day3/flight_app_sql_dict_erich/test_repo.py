import pytest
from db import db_setup
from db import repo_sql_dict as repo

@pytest.fixture(autouse=True)
def setup():
    db_setup.Base.metadata.drop_all(db_setup.engine)
    db_setup.Base.metadata.create_all(db_setup.engine)
    yield
    db_setup.Base.metadata.drop_all(db_setup.engine)

def test_create_flight():
    flight1 = {
        'id': 201,
        'airline': 'AirTest',
        'origin': 'NYC',
        'destination': 'LAX',
        'price': 299.99,
        'is_active': True
    }
    repo.create_flight(flight1)
    saved_flight = repo.read_by_id(201)
    assert saved_flight is not None
    assert saved_flight['airline'] == 'AirTest'
    assert saved_flight['origin'] == 'NYC'
    assert saved_flight['destination'] == 'LAX'
    assert saved_flight['price'] == 299.99