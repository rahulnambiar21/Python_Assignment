#Write a Python program to test whether a passed letter is a vowel or not.

str=input("Enter String :")

for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print("This is a Vowel")
    else:
        print("This is not a Vowel")
