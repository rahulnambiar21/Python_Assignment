#Write a Python program to convert a tuple to a string

def t1(t2):
    result = ''.join(t2)
    return result

my_tuple = ('H', 'e', 'l', 'l', 'o')
s1 = t1(my_tuple)
print(s1)
