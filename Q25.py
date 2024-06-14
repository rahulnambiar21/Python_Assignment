#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring  with 'good'.
#Return the resulting string

def replace(string):
    i1 = string.find('not')
    i2 = string.find('poor')

    if i1 != -1 and i2 != -1 and i1 < i2:
        string = string[:i1] + 'good' + string[i2 + 4:]

    return string

sentence = "He is not that poor today, but he was poor a long while ago."
result = replace(sentence)
print(result)
