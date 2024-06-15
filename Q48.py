#Write a Python script to concatenate following dictionaries to create a new one

def c1(*dicts):
    c2 = {}
    for d in dicts:
        c2.update(d)
    return c2

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

c2 = c1(dict1, dict2, dict3)
print("Concatenated dictionary:")
print(c2)
