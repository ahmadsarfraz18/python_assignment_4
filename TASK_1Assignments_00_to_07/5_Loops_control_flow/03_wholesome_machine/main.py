def main():
    AFFIRMATION = "I'm capable of doing anything I put my mind to. "

    print("Please type the following affirmation: ")
    print(AFFIRMATION)

    user_feedback = input(" > ")   

    while user_feedback != AFFIRMATION:      # Repeat until the correct affirmation is entered
        print("\nThat was not the affirmation. Try again! ")
        print("Please type the following affirmation: ")
        print(AFFIRMATION)

        user_feedback = input (" > ")
    
    print("\nThat's right! ")

if __name__ == "__main__":
    main()




