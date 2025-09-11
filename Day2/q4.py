names=input("enter names").split()
l1=sorted(names)
print(l1)
t1=tuple(l1)
print(t1)

filename="names_data.txt"
with open(filename, "w") as f:
    f.write("Sorted List: " + str(l1) + "\n")
    f.write("Sorted Tuple: " + str(t1) + "\n")
print({"filename": filename})   

print("\nReading back from file:")
with open(filename, "r") as f:
    data = f.read()
    print(data)