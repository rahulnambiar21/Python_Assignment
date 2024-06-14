#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#If the string length is less than 2, return instead of the empty string

def g1(s1):
    if len(s1) < 2:
        return ""
    else:
        return s1[:2] + s1[-2:]

input_str = "python"
print(g1(input_str))

input_str = "a"
print(g1(input_str))
