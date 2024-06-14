#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead
#if the string length of the given string is less than 3, leave it unchanged.

def a1(string):
    if len(string) >= 3:
        if string[-3:] == 'ing':
            new_string = string + 'ly'
        else:
            new_string = string + 'ing'
    else:
        new_string = string
    return new_string

s1 = "tag"
s2 = "jump"
s3 = "knowing"
s4 = "no"
print(a1(s1))  
print(a1(s2))
print(a1(s3))
print(a1(s4))
