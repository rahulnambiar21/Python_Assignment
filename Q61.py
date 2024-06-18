#Write a Python program to count the number of lines in a text file


def c1(f1):
    try:
        with open(f1, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1

        return line_count

    except FileNotFoundError:
        print(f"File '{f1}' not found.")

f1 = 'sample.txt'
num_lines = c1(f1)

if num_lines != -1:
    print(f"Number of lines in '{f1}': {num_lines}")
