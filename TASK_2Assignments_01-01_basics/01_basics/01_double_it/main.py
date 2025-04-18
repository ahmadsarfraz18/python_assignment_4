def main():
# Ask the user to enter a number

    curr_value = int(input("Enter a number: "))

        # Use a while loop to double the number until it is 100 or greater
    while curr_value < 100:
        # Double the curr_value
        curr_value = curr_value * 2
        # print the updated value
        print(curr_value, end = " ")
    
    # Print a newline at the end for better formatting
    print()

if __name__ == "__main__":
    main()

