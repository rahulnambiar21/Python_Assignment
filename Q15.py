#Write a Python function that takes two lists and returns true if they have at least one common member.

l1=[2,45,3,56,78]
l2=[3,10,90,102]

for i in l2:
    if i in l1:
        print("There is at least One common Element.")
        break
    else:
        print("There is no common Element.")
        break
