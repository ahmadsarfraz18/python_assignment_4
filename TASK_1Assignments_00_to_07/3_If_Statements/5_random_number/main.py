
import random  # Python ka built-in module jo random numbers generate karne ke liye use hota hai

def main():  # main function define kiya gaya hai

    N_NUMBERS = 10  # Total 10 random numbers generate karne hain
    MIN_VALUE = 1   # Random numbers ka minimum value 1 hoga
    MAX_VALUE = 100  # Random numbers ka maximum value 100 hoga

    # List comprehension ka use karke 10 random numbers generate kiye gaye hain jo 1 se 100 ke beech honge
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Random numbers ko string me convert karke space se join karke print kiya gaya hai
    print(" ".join(map(str, random_numbers)))

# Ye check karta hai ki program directly run ho raha hai ya kisi aur file se import ho raha hai
if __name__ == "__main__":
    main()  # Agar directly run ho raha ho toh main() function ko call karega
