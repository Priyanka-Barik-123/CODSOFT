import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, symbols=True):
    # Define character sets based on user input
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("Let's create a random password for you.")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 4 characters): "))
            if length < 4:
                print("Please enter a length of at least 4 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user input for character types
    uppercase = input("Include uppercase letters? (yes/no): ").lower() in ['yes', 'y']
    lowercase = input("Include lowercase letters? (yes/no): ").lower() in ['yes', 'y']
    digits = input("Include digits? (yes/no): ").lower() in ['yes', 'y']
    symbols = input("Include symbols? (yes/no): ").lower() in ['yes', 'y']

    # Generate the password based on user input
    password = generate_password(length, uppercase, lowercase, digits, symbols)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
