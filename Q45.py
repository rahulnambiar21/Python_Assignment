#Write a Python program to convert a list of tuples into a dictionary

def l1(tuple_list):

    d1 = {}

    for i in tuple_list:
        key, value = i
        d1[key] = value
    
    return d1

my_list = [(1, 'one'), (2, 'two'), (3, 'three')]

d2 = l1(my_list)
print("Converted dictionary:", d2)
