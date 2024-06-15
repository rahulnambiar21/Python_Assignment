#Write a Python script to check if a given key already exists in a dictionary.

def key_1(d, key):
    if d.get(key) is not None:
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3}
k2 = 'b'

if key_1(my_dict, k2):
    print(f"The key '{k2}' exists in the dictionary.")
else:
    print(f"The key '{k2}' does not exist in the dictionary.")
