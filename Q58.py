#•Write a Python program to read a file line by line and store it into a list

def r1(f1):
    lines = []
    try:
        with open(f1, 'r') as file:
            for line in file:
                lines.append(line.strip())

    except FileNotFoundError:
        print(f"File '{f1}' not found.")

    return lines

f1 = 'sample.txt'

lines = r1f1)

print(lines)
