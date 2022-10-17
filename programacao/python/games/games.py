import hangman
import guessing
from clear import clear_screen


def pick_game():
    display_opening_message()
    display_game_selection_menu()


def display_opening_message():
    print("""****************************)
*** Pick a game to play! ***
****************************
""")


def display_game_selection_menu():
    games = [("Guess", guessing), ("Hangman", hangman)]
    for index, game in enumerate(games):
        print(f"({index + 1}) {game[0]}")

    chosen = int(input("\nWhich game? ")) - 1

    clear_screen()
    games[chosen][1].play()


if __name__ == "__main__":
    pick_game()
