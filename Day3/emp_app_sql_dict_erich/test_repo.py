import pytest
from db import db_setup
from db import repo_sql_dict as repo
    


@pytest.fixture(autouse=True)
def setup():
    db_setup.Base.metadata.drop_all(db_setup.engine)  #drop all tables
    db_setup.Base.metadata.create_all(db_setup.engine)  #create tables
    yield
    db_setup.Base.metadata.drop_all(db_setup.engine)  #drop all tables after test

def test_create_employee():
    emp1={'id':110,'name':'Erich','age':30,'salary':5000.0,'is_active':True}
    repo.create_employee(emp1)
    savedEmp=repo.read_by_id(110)
    assert (savedEmp!=None)
    assert (savedEmp['id']==110)
    assert (savedEmp['name']=='Erich')
    assert (savedEmp['salary']==5000.0)
   