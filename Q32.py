#Write a Python program to check whether a list contains a sub list

def c1(m1, s1):
    main1 = tuple(m1)
    sub1 = tuple(s1)

    for i in range(len(main1) - len(sub1) + 1):
        if main1[i:i + len(sub1)] == sub1:
            return True
    return False

m1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]
sub2 = [3, 4, 5]
sub3 = [8, 1, 20]

print(c1(m1, sub2))
print(c1(m1, sub3))
