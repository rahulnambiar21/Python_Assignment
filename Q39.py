#Write a Python program to convert a list to a tuple

def l1(input_list):
    return tuple(input_list)

my_list = [1, 2, 3, 4, 5]

c1 = l1(my_list)
print("Converted tuple:", c1)
