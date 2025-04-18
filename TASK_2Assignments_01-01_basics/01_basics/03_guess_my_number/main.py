import random

# Generate a random number between 1 and 100

secret_number = random.randint(1 , 100)

# Print the initial message
print("I am thinking of a number between 1 and 100. Can you guess it?")

# Get the user's guess
guess = int(input('Enter your guess number: '))

# Keep asking for guesses until the user guesses the correct number

while guess != secret_number:
    if guess < secret_number:
        print("Too low Try again: ")
    
    else:
        print("Too high. Try again: ")

    print()

    guess = int(input("Enter your new guess number: "))

    print('Congrats! The number was: ', secret_number)

if __name__ == "__main__":
    main()
