#Write a Python program that will return true if the two given integer values are "equal" or their sum or difference is 5

a=int(input("Enter the First Number :"))+int(input("Enter the Second Number :"))
if a==5:
    print("Total:",a)
    print("True")
else:
    print("Total:",a)
    print("False")
    
b=int(input("Enter the First Number :"))-int(input("Enter the Second Number :"))

if b==5:
    print("Total:",b)
    print("True")
else:
    print("Total:",b)
    print("False")

if a==5 and b==5:
    print("True")
