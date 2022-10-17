import hangman.game as hangman
import guessing.game as guessing
from helpers.clear import clear_screen


def pick_game():
    display_opening_message()
    display_game_selection_menu()


def display_opening_message():
    print("""****************************)
*** Pick a game to play! ***
****************************
""")


def display_game_selection_menu():
    '''
    Prompts the player to choose a game and starts the chosen game.
    '''
    games = [("Guess", guessing), ("Hangman", hangman)]
    for index, game in enumerate(games):
        print(f"({index + 1}) {game[0]}")

    chosen = int(input("\nWhich game? ")) - 1

    clear_screen()
    games[chosen][1].play()


if __name__ == "__main__":
    pick_game()
