def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f'I am excited to add this {word} to vast collection of them! ')
    elif part_of_speech == 1:
        print(f'Its so nice outside today it makes me want to {word}! ')
    elif part_of_speech == 2:
        print(f'Looking outside of my window the sky is big {word}! ')
    else:
        print("Part of speech must be 0, 1, or 2! can't make a sentence")


def main():
    word = input("Please type a noun, verb or adjective: ")
    print("Is this a verb, noun or adjective? ")

    try: 
        part_of_speech = int(input("Please type 0 for verb 1 for noun or 2 for adjective: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("Invalid input! Please type 0, 1 or 2.")

if __name__ == "__main__":
    main()
    