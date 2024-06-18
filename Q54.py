#Write a Python program to read an entire text file

file_path = 'sample.txt'


with open(file_path, 'r') as file:
    file_content = file.read()
    print(file_content)
