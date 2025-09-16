import requests

BASE_URL = "http://localhost:5000"

def create_employee(employee):
    URL=f'{BASE_URL}/employees'
    response = requests.post(URL, json=employee)
    createdEmployee_dict=response.json()
    return createdEmployee_dict

def read_all_employee():
    URL=f'{BASE_URL}/employees'
    response = requests.get(URL)
    dict_employees=response.json()
    return dict_employees   


def  read_by_id(id):
    url=f'{BASE_URL}/employees/{id}'
    response = requests.get(url)
    employee_dict=response.json()
    return employee_dict

def update(id, new_employee):
    url=f'{BASE_URL}/employees/{id}'
    response = requests.put(url, json=new_employee)
    employee_dict=response.json()
    return employee_dict


def delete_employee(id):
    url=f'{BASE_URL}/employees/{id}'
    response = requests.delete(url)
    return response.json()