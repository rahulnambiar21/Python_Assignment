#Write a Python program to check whether an element exists within a tuple

def e1(input_tuple, element):
    return element in input_tuple

my_tuple = (1, 2, 3, 4, 5)

e2 = 3
if e1(my_tuple, e2):
    print(f"{e2} exists in the tuple")
else:
    print(f"{e2} does not exist in the tuple")

e3 = 6
if e1(my_tuple, e3):
    print(f"{e3} exists in the tuple")
else:
    print(f"{e3} does not exist in the tuple")
