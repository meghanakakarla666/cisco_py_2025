"""Employee App Main Module."""
import repo_sql_dict as repo

def create_employee_view():
    """View for creating an employee."""
    emp_id = int(input('ID:'))
    name = input('Name:')
    age = int(input('Age:'))
    salary = float(input('Salary:'))
    is_active = input('Active(y/n):').upper() == 'Y'

    employee = {'id':emp_id, 'name':name, 'age':age,'salary':salary, 'is_active':is_active}
    try:
        repo.create_employee(employee)
        print('Employee Created Successfully.')
    except repo.EmployeeAlreadyExistError as ex:
        print(f"{ex}")
    except repo.DatabaseError as ex:
        print(f"{ex}")

def list_all_employees_view():
    """View for listing all employees."""
    print('List of Employees:')
    for employee in repo.read_all_employee():
        print(employee)

def read_by_id_view():
    """View for reading an employee by ID."""
    emp_id = int(input('ID:'))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee not found.')
    else:
        print(employee)

def update_view():
    """View for updating an employee's salary."""
    emp_id = int(input('ID:'))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee Not Found')
    else:
        print(employee)
        salary = float(input('New Salary:'))
        new_employee = {
            'id': employee['id'],
            'name': employee['name'],
            'age': employee['age'],
            'salary': salary,
            'is_active': employee['is_active']
        }
        repo.update(emp_id, new_employee)
        print('Employee updated successfully.')

def delete_view():
    """View for deleting an employee."""
    emp_id = int(input('ID:'))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee Not Found')
    else:
        repo.delete_employee(emp_id)
        print('Employee Deleted Succesfully.')
def menu():
    """
    menu for operations wrt employee management
    """
    message = '''
Options are:
1 - Create Employee
2 - List All Employees
3 - Read Employee By Id
4 - Update Employee
5 - Delete Employee
6 - Exit 
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        create_employee_view()
        # emp_id = int(input('ID:'))
        # name = input('Name:')
        # age = int(input('Age:'))
        # salary = float(input('Salary:'))
        # is_active = input('Active(y/n):').upper() == 'Y'

        # employee = {'id':emp_id, 'name':name, 'age':age,'salary':salary, 'is_active':is_active}
        # try:
        #     repo.create_employee(employee)
        #     print('Employee Created Successfully.')
        # except repo.EmployeeAlreadyExistError as ex:
        #     print(f"{ex}")
        # except repo.DatabaseError as ex:
        #     print(f"{ex}")
    elif choice == 2:
        list_all_employees_view()
        # print('List of Employees:')
        # for employee in repo.read_all_employee():
        #     print(employee)
    elif choice == 3:
        read_by_id_view()
        # emp_id = int(input('ID:'))
        # employee = repo.read_by_id(emp_id)
        # if employee == None:
        #     print('Employee not found.')
        # else:
        #     print(employee)
    elif choice == 4:
        update_view()
        # emp_id = int(input('ID:'))
        # employee = repo.read_by_id(emp_id)
        # if employee == None:
        #     print('Employee Not Found')
        # else:
        #     print(employee)
        #     salary = float(input('New Salary:'))
        #     new_employee = {'id':employee['id'],
        #         'name':employee['name'],
        #         'age':employee['age'],
        #         'salary':salary,
        #         'is_active':employee['is_active']}
        #     repo.update(emp_id, new_employee)
        #     print('Employee updated successfully.')
    elif choice == 5:
        delete_view()
        # emp_id = int(input('ID:'))
        # employee = repo.read_by_id(emp_id)
        # if employee == None:
        #     print('Employee Not Found')
        # else:
        #     repo.delete_employee(emp_id)
        #     print('Employee Deleted Succesfully.')
    elif choice == 6:
        print('Thank you for using Application')

    return choice
def menus():
    """Main loop for the menu."""
    choice = menu()
    while choice != 6:
        choice = menu()

menus()
