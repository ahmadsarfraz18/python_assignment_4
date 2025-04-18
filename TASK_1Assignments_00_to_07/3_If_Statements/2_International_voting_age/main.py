

PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
   
    """Checks voting eligibility based on age"""

    user_age = int(input("Enter your age: "))

    if user_age >= PETURKSBOUIPO_AGE:
        print(f'You are {user_age} years old and eligible to vote PETURKSBOUIPO. ')
    else:
        print(f'You are {user_age} years old and not eligible to vote PETURKSBOUIPO. ')


    if user_age >= STANLAU_AGE:
        print(f'You are {user_age} years old and eligible to vote STANLAU. ')
    else: print (f'You are {user_age} years old and not eligible to vote STANLAU. ')


    if user_age >= MAYENGUA_AGE:
        print(f'You are {user_age} years old and eligible to vote MAYENGUA. ')
    else:
        print(f'You are {user_age} years old and not eligible to vote MAYENGUA. ')


if __name__ == "__main__":
    main()








