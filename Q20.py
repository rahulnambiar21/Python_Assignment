#Write a Python program to get unique values from a list  

def unique_value(l1):
    a = []
    for i in l1:
        if i not in a:
            a.append(i)
    return a

# Example usage
l1 = [1, 2, 3, 4, 2, 3, 5]
a = unique_value(l1)
print("Unique values:", a)
