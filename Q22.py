#Write a Python program to count the number of strings where the string length is 2 or more
#and the first and last character are same from a given list of strings

def count_strings(strings):
    c1 = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            c1 += 1
    return c1

l1 = ["bab", "xyz", "cc", "xyx", "bbb"]
print(count_strings(l1))
