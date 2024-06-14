#Write a Python program to split a list into different variables

def s1(l1):
    # Unpack the list into separate variables
    var1, var2, var3 = l1
    return var1, var2, var3

# Example usage:
my_list = [10, 20, 30]
v1, v2, v3 = s1(my_list)
print(v1)  # Output: 1
print(v2)  # Output: 2
print(v3)  # Output: 3
