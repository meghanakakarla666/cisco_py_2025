def find_min(salaries):
    min_salry=salaries[0]
    for salary in salaries:
        if salary<min_salry:
            min_salry=salary
    return min_salry

def find_max(salaries):
    max_salry=salaries[0]
    for salary in salaries:
        if salary>max_salry:
            max_salry=salary
    return max_salry

def find_total(salaries):
        total=0
        for salary in salaries:
            total+=salary
        return total

#driver code
salaries=[1000,2000,3000,4000,5000]
min_salary=find_min(salaries)
max_salary=find_max(salaries)
total_salary=find_total(salaries)
print(salaries)
print("min_salary:",min_salary)
print("max_salary:",max_salary)         
