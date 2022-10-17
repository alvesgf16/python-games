import random
from helpers.clear import clear_screen


def play():
    '''
    Guessing game loop.

    Each round, the player is asked to guess a number between 1 and 100. If
    they guess wrong, they are given a hint about how the secret number
    compares to their guess. If they get it right before running out of
    rounds, they win, otherwise they lose.
    '''
    secret_number = random.randrange(1, 101)
    total_rounds = set_game_difficulty()
    score = 100

    for current_round in range(1, total_rounds + 1):
        display_round_info(current_round, total_rounds)

        guess = ask_for_guess()

        if not is_guess_in_range(guess):
            print("You must enter a number between 1 and 100!")
            continue

        score = adjust_score(score, guess, secret_number)

        if guess == secret_number:
            print(f"You got it right and scored {score} points!")
            break
        else:
            if current_round == total_rounds:
                print(
                    f"The secret number was {secret_number}. "
                    f"You scored {score} points."
                )
                print("Game over")
            else:
                display_hints(guess, secret_number)


def display_opening_message():
    print(
        """*****************************
Welcome to the Guessing game!
*****************************
"""
    )


def set_game_difficulty():
    '''
    Prompts the player to choose a difficulty and sets the number of rounds
    for the game accordingly.
    '''
    total_rounds = 0

    display_opening_message()
    print("Which difficulty?")
    print("(1) Easy   (2) Medium   (3) Hard")

    while total_rounds == 0:
        rounds_per_difficulty = {"1": 20, "2": 10, "3": 5}
        difficulty = input("Choose a level: ")

        if difficulty in rounds_per_difficulty.keys():
            total_rounds = rounds_per_difficulty[difficulty]
        else:
            continue

    clear_screen()
    return total_rounds


def display_round_info(current_round, total_rounds):
    print(f"Round {current_round} of {total_rounds}")


def ask_for_guess():
    guess_str = input("Enter a number between 1 and 100: ")

    clear_screen()

    print("You entered", guess_str)
    return int(guess_str)


def is_guess_in_range(guess):
    lower_limit = 1
    upper_limit = 100

    return lower_limit < guess < upper_limit


def adjust_score(score, guess, secret_number):
    '''
    Subtracts the difference between the guess and the secret number from the
    score.
    '''
    lost_points = abs(secret_number - guess)
    score -= lost_points
    return score


def display_hints(guess, secret_number):
    if guess > secret_number:
        print(
            """You missed! Your guess was bigger than the secret number.
"""
        )
    elif guess < secret_number:
        print(
            """You missed! Your guess was smaller than the secret number.
"""
        )


if __name__ == "__main__":
    play()
