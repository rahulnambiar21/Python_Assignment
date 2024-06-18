#•Write a python program to find the longest words

def f1(f2):
    try:
        with open(f2, 'r') as file:
            content = file.read()
            words = content.split()
            longest_words = []
            max_length = 0
            for word in words:
                word = word.strip(",.?!")
                word_length = len(word)
                if word_length > max_length:
                    longest_words = [word]
                    max_length = word_length
                elif word_length == max_length:
                    longest_words.append(word)

            return longest_words

    except FileNotFoundError:
        print(f"File '{f2}' not found.")
        return []
f2 = 'sample.txt'
longest_words = f1(f2)
if longest_words:
    print(f"The longest words in '{f2}' are:")
    for word in longest_words:
        print(word)
else:
    print("No words found in the file.")
