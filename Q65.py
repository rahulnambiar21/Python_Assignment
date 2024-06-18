#Write a Python program to write a list to a file

def write_list_to_file(lst, filename):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(str(item) + '\n')
        print(f"List has been written to {filename} successfully.")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

my_list = ['apple', 'banana', 'cherry', 'date']
file_name = 'sample.txt'

write_list_to_file(my_list, file_name)
