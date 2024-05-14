#Write a Python function to get the largest number, smallest num and sum of all from a list.

import random

l=[]

for i in range(1,51):
        l.append(i)

print(l)
print("Minimum = ",min(l))
print("Maximum = ",max(l))

total=sum(l)

print("Sum of the ginen List = ", total)
