import random

def high_low_game():
    print("Welcome to the High-Low Game!")
    
    rounds = int(input("How many rounds would you like to play? "))
    score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num} of {rounds}")
        
        # Generate numbers
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is: {your_number}")

        # User makes a guess
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").lower()

        # Determine result
        if (guess == "higher" and your_number > computer_number) or \
           (guess == "lower" and your_number < computer_number):
            print("Correct guess! You get a point.")
            score += 1
        else:
            print("Wrong guess!")
        
        print(f"The computer's number was: {computer_number}")
        print(f"Current score: {score}")

    print("\nGame over!")
    print(f"Your final score is: {score} out of {rounds}")

# Start the game
high_low_game()
