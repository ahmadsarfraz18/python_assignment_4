def get_user_info():

    #   """
    # Asks the user for their first name, last name, and email address,
    # then returns these as a tuple.
    # """

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")

    return first_name, last_name, email


def main():

    user_info = get_user_info()
    print("Received the following informatation from the user: ", user_info)


if __name__ == "__main__":
    main()
