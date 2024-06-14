#Write a Python function that takes a list of words and returns the length of the longest one

def l1(word_list):
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)

    return max_length

words = ["Hinata", "Asahi", "Tanjiro", "Kageyama"]
print(l1(words))
