import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    num = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user choice (you can customize this)
    all_chars = lc + uc + num + special_chars

    # Check if the length is valid
    if length < 4:
        print("Password length must be at least 4 characters.")
        return None

    # Generate the password
    password = random.sample(all_chars, length - 3)  # Leave 3 characters for lowercase, uppercase, and digit
    password += random.choice(lc)
    password += random.choice(uc)
    password += random.choice(num)
    random.shuffle(password)
    password = ''.join(password)

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired length of the password: "))
        generated_password = generate_password(password_length)
        if generated_password:
            print("Generated Password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
