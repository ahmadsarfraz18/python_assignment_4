def greet(name: str) -> str:
    return "Assalamualaikum, " + name + "!"

def main():
    name = input("What is your name? ")
    print(greet(name))

if __name__ == "__main__":      
    main()