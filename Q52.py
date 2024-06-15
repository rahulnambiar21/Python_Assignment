#Write a Python program to check multiple keys exists in a dictionary

def c1(d, keys):
    for key in keys:
        if key not in d:
            return False
    return True

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
k1 = ['b', 'c', 'e']

if c1(my_dict, k1):
    print("All keys exist.")
else:
    print("Not all keys exist.")
