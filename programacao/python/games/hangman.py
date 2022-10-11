def play():
    print("****************************")
    print("Welcome to the Hangman game!")
    print("****************************")

    secret_word = "banana"
    guessed_letters = ["_" for character in range(len(secret_word))]

    hanged = False
    guessed = False

    print(guessed_letters)

    while not hanged and not guessed:
        guess = input("Which letter? ")
        guess = guess.strip()

        for index, letter in enumerate(secret_word):
            if guess.upper() == letter.upper():
                guessed_letters[index] = letter

        print(guessed_letters)

    print("Game over")


if __name__ == "__main__":
    play()
