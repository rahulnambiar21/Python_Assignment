#Write a Python script to merge two Python dictionaries

def m1(dict1, dict2):
    m2 = dict1.copy()
    m2.update(dict2)
    return m2

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4, 'e':5}
m2 = m1(dict1, dict2)

print("Merged dictionary:")
print(m2)
