#Write a Python function to insert a string in the middle of a string

def insert_string(m1, insert_string):
    m2 = len(m1) // 2
    return m1[:m2] + insert_string + m1[m2:]


main_str = "Hello  there!"
insert_str = "world"
print(insert_string(main_str, insert_str))
