import random
import string


def generate_password(length):
    # Define the character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all the character sets
    all_chars = lower + upper + digits + special

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all character sets
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list to ensure random order
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)


def main():
    print("Secure Password Generator")
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        if length < 4:4
            print("Password length should be at least 4 characters to ensure complexity.")
            return

        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            print(generate_password(length))
    except ValueError:
        print("Please enter valid numbers for length and quantity.")


if __name__ == "__main__":
    main()
