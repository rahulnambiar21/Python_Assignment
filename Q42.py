#Write a Python program to find the repeated items of a tuple

def f1(input_tuple):

    input_list = list(input_tuple)
    c1 = {}

    for i in input_list:
        c1[i] = c1.get(i, 0) + 1
    
    r1 = [i for i, count in c1.items() if count > 1]
    
    return r1

my_tuple = (1, 2, 3, 4, 1, 2, 5, 6, 3)

r1 = f1(my_tuple)
print("Repeated items:", r1)
