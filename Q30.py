#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string

def s1(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    result = new_str1 + ' ' + new_str2
    return result

string_1 = "Tops"
string_2 = "Technologies"
print(s1(string_1, string_2))
