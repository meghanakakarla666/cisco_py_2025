#1.testing the repo.py file
from repo import create_employee, read_all_employees, read_by_id
from repo import update, delete_employee


import repo
employee = (101,'Banu', 22, 50000, True)
repo.create_employee(employee)
print(f'employee {employee} created successfully')

print('after adding all employees:', repo.read_all_employees())


employee = (102,'Mahesh', 46, 4000.50, True)
repo.create_employee(employee)
print(f'employee {employee} created successfully')
print('after adding all employees:', repo.read_all_employees())

employee = (103,'Vaishnavi', 21, 40000.75, True)
repo.create_employee(employee)
print(f'employee {employee} created successfully')
print('after adding all employees:', repo.read_all_employees())


employee = repo.read_by_id(103)
if employee==None:
    print('Employee not found')
else:
    print('employee found:', employee)
    

#test uopdate
employee=repo.read_by_id(103)
if employee==None:
    print('Employee not found')
else:
    id,name,age,salary,is_active=employee
    salary+=20000
    new_employee = (id,name,age,salary,is_active)
    repo.update(103,new_employee)
    print('after update:', repo.read_all_employees())

#test delete        
repo.delete_employee(102)
print('after delete:', repo.read_all_employees())
#2.make as app