numbers=list(map(int,input("enter numbers:").split()))
list=numbers
total=sum(list)
average=total/len(list)
print("list:",list)
print("total:",total)
print("average:",average)

file_name="numbers_data.txt"
with open(file_name,"w") as f:
    f.write(f'List:{list}\n')
    f.write(f'Total:{total}\n')
    f.write(f'Average:{average}\n')

with open(file_name,"r") as reader:
    data=reader.read()
    print(data)