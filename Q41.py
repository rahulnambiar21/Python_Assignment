#Write a Python program to replace last value of tuples in a list

def r1(t1, new_value):
    for i in range(len(t1)):
        temp_list = list(t1[i])
        temp_list[-1] = new_value
        t1[i] = tuple(temp_list)
    return t1

# Example usage:
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_value = 200
modified_list = r1(my_list, new_value)
print("Modified list:", modified_list)
