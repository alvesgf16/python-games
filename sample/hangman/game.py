import random
from helpers.clear import clear_screen


def play():
    '''
    Hangman game loop.

    Initially, a secret word is chosen from a file of words and its length is
    shown to the player as a string of blank lines (underscores), together with
    the gallows in its initial stage.

    Then, with each round until the player has either guessed the secret word
    or made 6 mistakes, they are prompted to guess a letter. If they guessed
    correctly, the letter is shown to them in every position where it appears
    in the secret word, else the gallows drawing is updated with a body part.

    Finally, the outcome of the game is shown to the player.
    '''
    secret_word = load_secret_word()
    guessed_letters = initialize_guessed_letters(secret_word)
    errors = 0
    hanged = False
    guessed = False

    display_opening_message()
    draw_hangman(errors)
    print(" ".join(guessed_letters))

    while not hanged and not guessed:
        guess = ask_for_guess()

        if guess in secret_word:
            mark_correct_guess(guess, guessed_letters, secret_word)
        else:
            errors += 1

        clear_screen()
        display_opening_message()
        draw_hangman(errors)
        print(" ".join(guessed_letters))

        hanged = errors == 6
        guessed = "_" not in guessed_letters

    if guessed:
        display_victory_message(secret_word)
    else:
        display_defeat_message(secret_word)


def display_opening_message():
    print(
        """****************************
Welcome to the Hangman game!
****************************
"""
    )


def load_secret_word(filename="sample/hangman/words.txt", first_valid_line=0):
    '''
    Randomly select a word from a file. The file should contain one word per
    line.

        Parameters:
            filename (str): The absolute pathname of the file from which the
                            words will be drawn
            first_valid_line (int): The first line in the file to be included
                                    in the draw

        Returns:
            secret_word (str): The selected word in all capital letters
    '''
    with open(filename, "r") as file:
        words = [line.strip() for line in file]

    secret = random.randrange(first_valid_line, len(words))
    secret_word = words[secret].upper()
    return secret_word


def initialize_guessed_letters(word):
    '''Returns a list of blank lines for each letter in the word.'''
    return ["_" for _ in range(len(word))]


def ask_for_guess():
    guess = input("Guess a letter: ")
    guess = guess.strip().upper()
    return guess


def mark_correct_guess(guess, guessed_letters, secret_word):
    '''
    Add correct guesses to their correct positions in the guessed_letters list.

        Parameters:
            guess (str): The letter guessed by the player
            guessed_letters (list): A list of guessed letters/blank lines
            secret_word (str): Thw secret word to be guessed
    '''
    for index, letter in enumerate(secret_word):
        if guess == letter:
            guessed_letters[index] = letter


def draw_hangman(errors):
    '''Receives the number of errors the player has made and prints the
    corresponding gallows stage'''
    stages = [
        """ |
 |
 |
 |""",
        """ |      (_)
 |
 |
 |""",
        """ |      (_)
 |       |
 |       |
 |""",
        """ |      (_)
 |      \\|
 |       |
 |""",
        """ |      (_)
 |      \\|/
 |       |
 |""",
        """ |      (_)
 |      \\|/
 |       |
 |      /""",
        """ |      (_)
 |      \\|/
 |       |
 |      / \\""",
    ]
    print(
        f"""  _______
 |/      |
{stages[errors]}
 |
_|___
"""
    )


def display_victory_message():
    print(
        """       ___________
      '._==_==_=_.'
      .-\\\\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \\\\::.   /
         '::. .'
           ) (
         _.' '._
        '-------'
Congratulations, you won!"""
    )


def display_defeat_message(secret_word):
    print(
        f"""    _______________
   /               \\
  /                 \\
//                   \\/\\
\\|   XXXX     XXXX   | /
 |   XXXX     XXXX   |/
 |   XXX       XXX   |
 |                   |
 \\__      XXX      __/
   |\\     XXX     /|
   | |           | |
   | I I I I I I I |
   |  I I I I I I  |
   \\_             _/
     \\_         _/
       \\_______/
Gosh, you've been hanged!
The secret word was {secret_word}"""
    )


if __name__ == "__main__":
    play()
