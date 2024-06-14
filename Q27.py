#Write a Python function to reverses a string if its length is a multiple of 4

def r1(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]
    else:
        return input_string


input_str = "abcdef"
print(r1(input_str))

input_str = "abcdefgh"
print(r1(input_str))
