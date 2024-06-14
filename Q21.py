#Write a Python function that takes a list and returns a new list with unique elements of the first list

def e1(l1):
    u1 = []
    for i in l1:
        if i not in u1:
            u1.append(i)
    return u1


l2 = [1, 2, 2, 3, 4, 4, 5]
print(e1(l2))
