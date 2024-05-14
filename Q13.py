#Write a Python program to remove duplicates from a list

list1=[22,45,65,85,2,22,98,100,65,2,45]

print("This is List1 : ",list1)

list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

print("The new List after removing duplicates is : ",list2)
