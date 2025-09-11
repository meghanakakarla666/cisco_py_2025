class EmployeeException(Exception):
    pass

class EmployeeNotFoundError(EmployeeException):
    pass

class EmployeeAlreadyExitError(EmployeeException):
    pass

class DatabaseError(EmployeeException):
    pass

