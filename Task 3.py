import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for complexity."

    # Character sets to include
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation

    # Ensure the password has at least one character from each set
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(specials)
    ]

    if length > 4:
        all_chars = lowercase + uppercase + digits + specials
        password_chars += random.choices(all_chars, k=length-4)

    # Shuffle the result list to avoid predictable sequences
    random.shuffle(password_chars)

    # Join list elements to form the password string
    return ''.join(password_chars)

def main():
    print("Strong Password Generator")

    while True:
        try:
            length = int(input("Enter desired password length (min 4): "))
            if length < 4:
                print("Password length too short. Please enter 4 or higher.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
