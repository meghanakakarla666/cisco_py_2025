employees=[]
employee=('banau',22,5000,True)
employees.append(employee)
employee=('Mahesh',46,4000.50,True)
employees.append(employee)
employee=('vaishnavi',21,4000.75,True)
employees.append(employee)

i=0
search="vaishnavi"  
index=-1
for emp in employees:
    if emp[0]==search:
        index=i
        break
    i+=1
if index=-1:
    print("Employee not found")
else:
    print("Employee found at index",index)

    print(employees[index])
    search_employee=employees[index]
    print("Name:",search_employee)
    salary=float(input('salary'))

