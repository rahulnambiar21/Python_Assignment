#Write a Python program to read a file line by line store it into a variable

def r1(f1):
    file_content = ""
    try:
        with open(f1, 'r') as file:
            for line in file:
                file_content += line

    except FileNotFoundError:
        print(f"File '{f1}' not found.")

    return file_content

f1 = 'sample.txt'
content = r1(f1)
print(content)
