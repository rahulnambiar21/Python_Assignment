#Write a Python program to read last n lines of a file

def r1(f1, n):
    try:
        with open(f1, 'r') as file:
            lines = file.readlines()
        start = max(0, len(lines) - n)
        for line in lines[start:]:
            print(line, end='')  

    except FileNotFoundError:
        print(f"File '{f1}' not found.")
f1 = 'sample.txt'
n = 1

r1(f1, n)
