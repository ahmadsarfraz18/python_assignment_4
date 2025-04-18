# A simple program to determine if a person is tall enough to ride a rollercoaster

MINIMUM_HEIGHT: int = 50

def main():
    height: float = float(input("How tall are you? "))  # Type conversion added

    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride.")
    else: 
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()
