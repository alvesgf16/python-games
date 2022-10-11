import random


def play():
    print("****************************")
    print("Welcome to the Hangman game!")
    print("****************************")

    with open("words.txt", "r") as file:
        words = [line.strip() for line in file]

    secret = random.randrange(0, len(words))
    secret_word = words[secret].upper()

    guessed_letters = ["_" for _ in range(len(secret_word))]

    errors = 0
    hanged = errors == 6
    guessed = "_" not in guessed_letters

    print(guessed_letters)

    while not hanged and not guessed:
        guess = input("Which letter? ")
        guess = guess.strip().upper()

        if guess in secret_word:
            for index, letter in enumerate(secret_word):
                if guess == letter:
                    guessed_letters[index] = letter
        else:
            errors += 1
            print(f"Oops, you're wrong! {6 - errors} to go")

        print(guessed_letters)

    if guessed:
        print("You won!")
    else:
        print("You lost.")
    print("Game over")


if __name__ == "__main__":
    play()
