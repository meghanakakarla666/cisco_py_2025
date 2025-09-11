words=input("enter words:")
words_list=words.split(" ")
words_tuple=tuple(words_list)
print(words)
print(words_list)
print(words_tuple)

file_name=input("enter file name:")
with open(file_name,"w") as f:
    f.write(f'List:{words_list}\n')
    f.write(f'Tuple:{words_tuple}\n')

with open(file_name,"r") as reader:
    line_list=reader.readline()
    line_tuple=reader.readline()
    print(line_tuple)
    print(line_list)