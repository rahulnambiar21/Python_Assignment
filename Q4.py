#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
d=a+b+c
if a==0 and b==0:
    print("Sum is zero")
elif b==0 and c==0:
    print("Sum is zero")
elif a==0 and c==0:
    print("Sum is zero")
else:
    print("Total :",d)


      
      
