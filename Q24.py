#Write a Python program to count the occurrences of each word in a given sentence

def count_word(s1):
    w1 = s1.split()
    w2 = {}
    
    for word in w1:
        w2[word] = w2.get(word, 0) + 1
    return w2

s1 = "Hello World, This is tops technologies."
w3 = count_word(s1)
for word, count in w3.items():
    print(f"{word}: {count}")
