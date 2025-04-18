
import random

def main():
    # Generate the secret number at random
    secret_number = random.randint(1, 99)
    print('I am thinking of a number between 1 and 99...')

    # Get the user's first guess
    guess = int(input('What is your guess? '))

    # Loop until the user guesses the correct secret number
    while guess != secret_number:
        if guess < secret_number: 
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')

        print()
        guess = int(input('Enter your new guess number: '))

    print('🎉 You got it! The secret number was', secret_number)

# Call the main function
if __name__ == "__main__":
    main()

