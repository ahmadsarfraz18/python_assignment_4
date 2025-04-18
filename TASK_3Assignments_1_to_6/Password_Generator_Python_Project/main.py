

import random
import string

def generate_password(length):
    """ Generate a random password of the specified length. """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("=======================")

    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    try:
        length_password = int(input("Enter the length of each password: "))
        if length_password <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(length_password)
        print(f'Password {i + 1}: {password}')

    play_again = input("\nDo you want to generate more passwords? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thank you for using the Password Generator! Goodbye!")

if __name__ == "__main__":
    main()
