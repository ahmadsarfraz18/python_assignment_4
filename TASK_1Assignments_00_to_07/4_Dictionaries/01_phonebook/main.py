# Function to read name and number from the user and store them in a dictionary (phonebook)
def read_phone_numbers():
    """ Ask the user for name/number to store in the phonebook (Dictionary) and return the phonebook """
    
    phonebook = {}  # Empty dictionary to store name-number pairs

    while True:
        name = input("Name: ")  # Ask user for a name
        if name == "":  # If input is empty, break the loop
            break
        number = input("Number: ")  # Ask user for a number
        phonebook[name] = number  # Store the name and number in the dictionary

    return phonebook  # Return the filled phonebook


# Function to print all name-number pairs in the phonebook
def print_phonebook(phonebook):
    """ Prints out all the name/numbers in the phonebook (Dictionary) """

    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))  # Print each name and its associated number


# Function to look up a number by name from the phonebook
def lookup_numbers(phonebook):
    """ Allow the user to look up a number in the phonebook by providing the name """

    while True:
        name = input("Enter the name to lookup: ")  # Ask for the name to look up
        if name == "":  # If input is empty, exit the loop
            break
        if name not in phonebook:
            print(name + " is not in the phonebook.")  # If name not found, print message
        else:
            print(phonebook[name])  # If name found, print the associated number


# Main function to run the program flow
def main():
    phonebook = read_phone_numbers()     # Step 1: Read name-number pairs from the user
    print_phonebook(phonebook)           # Step 2: Print the complete phonebook
    lookup_numbers(phonebook)            # Step 3: Allow user to search for numbers


# Standard Python entry point to call main() only when script is run directly
if __name__ == "__main__":
    main()
