def average(a: float, b: float) -> float:

    """Return the number which is between a and b """

    return (a + b) / 2

def main():
    print("Average calculation program! ")

    num1 = float(input("Enter the first number! "))
    num2 = float(input("Enter the second number! "))

    average_result = average (num1, num2)
    print(f'The average of {num1} and {num2} is: {average_result}! ') 

if __name__ == "__main__":
    main()

