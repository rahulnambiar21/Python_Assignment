#Write a Python script to print a dictionary where the keys are numbers between 1 and 15

def c1():
    d1 = {}
    for i in range(1, 16):
        d1[i] = i * 2
    return d1

d1 = c1()
print(d1)
