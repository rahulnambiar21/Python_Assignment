#Write a Python program to copy the contents of a file to another file

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except IOError as e:
        print(f"Error: {e}")

# Example usage:
source_file = 'sample.txt'
destination_file = 'destination.txt'

copy_file(source_file, destination_file)
