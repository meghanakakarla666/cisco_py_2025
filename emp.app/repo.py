
#crud operations (create, read, update, delete)

employees=[] #(id, name, age, salary, is_active)


def create_employee(employee):
    global employees
    employees.append(employee)

def read_all_employees():
    return employees

def read_by_id(id):
    for employee in employees:
        if employee[0]==id:
            return employee
    return None

def update(id, employee):
    I=0
    for employee in employees:
        if employee[0]==id:
            employees[I]=employee
            break
        I+=1

def delete_employee(id):
    index=-1
    I=0
    for employee in employees:
        if employee[0]==id:
            index=I
            break
        I+=1
    if index!=-1:
        employees.pop(index)