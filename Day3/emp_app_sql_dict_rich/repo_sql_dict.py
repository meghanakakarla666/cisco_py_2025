from db_setup import session,Employee
from log import logging
from sqlalchemy.exc import SQLAlchemyError,IntegrityError



#CRUD (Create, Read All | Read One, Update, Delete)
#Employee App -SQL DB -diict element

def create_employee(employee):

    try:
        employee_model = Employee(
            id=employee['id'],
            name=employee['name'],
            age=employee['age'],
            salary=employee['salary'],
            is_active=employee['is_active']
        )
        session.add(employee_model)  #insert stmt db
        session.commit()
        logging.info("employee created successfully")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate employee id:%s",ex)
        raise
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("database Error occurred while creating employee:%s",ex)
        raise

def read_all_employee():
    employees = session.query(Employee).all()
    dict_employees=[]
    for employee in employees:
        employee_dict={'id':employee.id,'name':employee.name,'age':employee.age,
                       'salary':employee.salary,'is_active':employee.is_active}
        dict_employees.append(employee_dict)
    logging.info("read all employees.")
    return dict_employees

def read_modal_by_id(id):
    employee = session.query(Employee).filter(Employee.id == id).first()
    logging.info("read employee model.")
    return employee

def  read_by_id(id):
    employee=read_modal_by_id(id)
    if not employee:
        logging.info("employee with id={id} not found")
        return None
    employee_dict={'id':employee.id,'name':employee.name,'age':employee.age,
                   'salary':employee.salary,'is_active':employee.is_active}
    logging.info("read employee for given id.")
    return employee_dict


def update(id, new_employee):
    employee=read_modal_by_id(id)
    if not employee:
        logging.info("employee with id={id} not found")
        return None
    employee.salary=new_employee['salary']
    session.commit()
    logging.info("employee with id={id} updated successfully")
    return new_employee
    
           
    
def delete_employee(id):
    employee=read_modal_by_id(id)
    if not employee:
        logging.info(f"employee not found {id}.")
        return None
    session.delete(employee)
    session.commit()
    logging.info("employee with id={id} deleted successfully")