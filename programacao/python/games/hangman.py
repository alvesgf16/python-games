def play():
    print("****************************")
    print("Welcome to the Hangman game!")
    print("****************************")

    secret_word = "banana"

    hanged = False
    guessed = False

    while not hanged and not guessed:
        guess = input("Which letter? ")
        guess = guess.strip()

        for index, letter in enumerate(secret_word):
            if guess.upper() == letter.upper():
                print(f"Letter {letter} found at position {index}")

    print("Game over")


if __name__ == "__main__":
    play()
