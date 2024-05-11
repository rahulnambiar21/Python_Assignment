# Write a Python program to get the Fibonacci series of given range.

n=int(input("Enter Number: "))
a,b=0,1
print(a,end=" ")
for i in range(2,n):
    if b<n:
        print(b,end=" ")
        a,b=b,a+b
    else:
        break
print()



        
