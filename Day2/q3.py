sentence = input("enter the sentence: ")
words_list = sentence.split()
words_tuple = tuple(word.upper() for word in words_list)
filename = "sentence_data.txt"

with open(filename, "w") as f:
    f.write("Words List: " + str(words_list) + "\n")
    f.write("Words Tuple UPPERCASE: " + str(words_tuple) + "\n")

print({"filename": filename})

print("\nReading back from file:")
with open(filename, "r") as f:
    data = f.read()
    print(data)