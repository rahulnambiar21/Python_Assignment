#Write a Python program to remove an empty tuple(s) from a list of tuples

def r1(tuple_list):
    return [i for i in tuple_list if i]

my_list = [(1, 2), (), (3, 4), (), (), (5, 6, 7), (), (8, 9)]

f1 = r1(my_list)
print("List after removing empty tuples:", f1)
