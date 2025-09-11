# Problem 5

# Step 1: Read a sequence of numbers from user input
numbers_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert to list of integers
numbers_list = [int(num) for num in numbers_input.split()]

# Step 3: Find max and min
maximum = max(numbers_list)
minimum = min(numbers_list)

# Step 4: Save list, max, and min to a file
with open("minmax_data.txt", "w") as file:
    file.write("List of Numbers:\n")
    file.write(str(numbers_list) + "\n")
    file.write(f"Maximum: {maximum}\n")
    file.write(f"Minimum: {minimum}\n")

# Step 5: Read and print data from the file
with open("minmax_data.txt", "r") as file:
    content = file.read()

print("\n--- Contents of 'minmax_data.txt' ---")
print(content)
