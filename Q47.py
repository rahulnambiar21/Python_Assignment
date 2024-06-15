#Write a Python script to sort (ascending and descending) a dictionary by value

def s1(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

my_dict = {'red': 5, 'orange': 3, 'blue': 8, 'black': 1}
s1 = s1(my_dict)

print("Dictionary in ascending order:")
for key, value in s1.items():
    print(f"{key}: {value}")

def s3(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

my_dict = {'apple': 10, 'banana': 8, 'orange': 1, 'pear': 31}
s4 = s3(my_dict)

print("\nDictionary in descending order:")
for key, value in s4.items():
    print(f"{key}: {value}")
