#Write a Python program to count occurrences of a substring in a string

def count_substring(main, sub1):
    return main.count(sub1)

# Example usage:
main = "hello world hello world hello world"
sub1 = "hello"
print(count_substring(main, sub1))
