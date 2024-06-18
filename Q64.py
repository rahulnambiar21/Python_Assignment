#Write python program that user to enter only odd numbers, else will raise an exception

def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 1:
                return num
            else:
                raise ValueError("You must enter an odd number.")
        except ValueError as ve:
            print(ve)

try:
    odd_number = get_odd_number()
    print(f"You entered an odd number: {odd_number}")
except ValueError:
    print("Invalid input. Please enter an odd number.")
