import hangman
import guessing
from clear import clear_screen


def pick_game():
    display_opening_message()
    display_game_selection_menu()


def display_opening_message():
    print("****************************")
    print("*** Pick a game to play! ***")
    print("****************************")


def display_game_selection_menu():
    print("(1) Hangman   (2) Guess")

    game = int(input("Which game?"))

    if game == 1:
        clear_screen()
        hangman.play()
    elif game == 2:
        clear_screen()
        guessing.play()


if __name__ == "__main__":
    pick_game()
