#Write a Python program to unzip a list of tuples into individual lists

def u1(tuple_list):
    l1 = zip(*tuple_list)
    l2 = [list(i) for i in l1]
    return l2

my_list = [(1, 2, 3), ('a', 'b', 'c'), (True, False, True)]

l1 = u1(my_list)
print("Unzipped lists:", l1)
