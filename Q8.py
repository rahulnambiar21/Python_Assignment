# Write a Python Program to get the Factorial number of a given number.

n=int(input("Enter N : "))
fac=1
for i in range(n,1,-1):
    fac=fac*i
print("Factorial : ",fac)
