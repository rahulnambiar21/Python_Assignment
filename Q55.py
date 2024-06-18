#Write a Python program to append text to a file and display the text

f1 = 'sample.txt'
text1 = "Hello World.\n"

with open(f1, 'a') as file:
    file.write(text1)

print(f"Appended text: {text1}")
with open(f1, 'r') as file:
    updated_content = file.read()
    print(f"\nUpdated File Content:\n{updated_content}")
