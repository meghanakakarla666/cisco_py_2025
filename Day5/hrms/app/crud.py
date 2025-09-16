from app.models import db,Employee

def create_employee(employee):
    employee_model = Employee(
        id=employee['id'],
        name=employee['name'],
        age=employee['age'],
        salary=employee['salary'],
        is_active=employee['is_active']
    )
    db.session.add(employee_model)  #insert stmt db
    db.session.commit()
    

def read_all_employee():
    employees = db.session.query(Employee).all()
    dict_employees=[]
    for employee in employees:
        employee_dict=employee.to_dict()
         #{'id':employee.id,'name':employee.name,'age':employee.age,
         #              'salary':employee.salary,'is_active':employee.is_active}
         # above can be replaced by to_dict method in model class
         # whenever u want dict representation of model class object
         # just call to_dict method
         # employee.to_dict()
         # instead of writing the same code again and again
         # this is code reusability
         # also if u want to change the dict representation
         # u just need to change in one place
         # in to_dict method of model class
         # not in all places where u want dict representation
        dict_employees.append(employee_dict)
    return dict_employees

def read_modal_by_id(id):
    employee = db.session.query(Employee).filter(Employee.id == id).first()
    return employee

def  read_by_id(id):
    employee=read_modal_by_id(id)
    if not employee:
        return None
    employee_dict=employee.to_dict()
    return employee_dict


def update(id, new_employee):
    employee=read_modal_by_id(id)
    if not employee:
        return None
    employee.salary=new_employee['salary']
    db.session.commit()


def delete_employee(id):
    employee=read_modal_by_id(id)
    if not employee:
        return None
    db.session.delete(employee)
    db.session.commit()