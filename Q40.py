#Write a Python program to reverse a tuple

def r1(input_tuple):
    return input_tuple[::-1]

# Example usage:
my_tuple = (1, 2, 3, 4, 5)

r2 = r1(my_tuple)
print("Reversed tuple:", r2)
