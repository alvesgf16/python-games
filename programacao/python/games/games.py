# import hangman
import guessing


def pick_game():
    print("****************************")
    print("*** Pick a game to play! ***")
    print("****************************")

    print("(1) Hangman   (2) Guess")

    game = int(input("Which game?"))

    if game == 1:
        print("Under construction, come back later")
        # hangman.play()
    elif game == 2:
        guessing.play()


if __name__ == "__main__":
    pick_game()
