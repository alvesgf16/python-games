import random
from clear import clear_screen


def play():
    secret_number = random.randrange(1, 101)
    score = 100

    display_opening_message()
    total_rounds = set_game_difficulty()

    for round_number in range(1, total_rounds + 1):
        display_round_info(round_number, total_rounds)

        guess = ask_for_guess()

        if guess < 1 or guess > 100:
            print("You must enter a number between 1 and 100!")
            continue

        if guess == secret_number:
            print(f"You got it right and scored {score} points!")
            break
        else:
            adjust_score(score, guess, secret_number)

            if round_number == total_rounds:
                print(f"The secret number was {secret_number}. You scored {score} points.")
            else:
                display_hints(guess, secret_number)

    print("Game over")


def display_opening_message():
    print("""*****************************
Welcome to the Guessing game!
*****************************
""")


def set_game_difficulty():
    total_rounds = 0

    print("Which difficulty?")
    print("(1) Easy   (2) Medium   (3) Hard")

    while total_rounds == 0:
        difficulty = int(input("Choose a level: "))

        if difficulty == 1:
            total_rounds = 20
        elif difficulty == 2:
            total_rounds = 10
        elif difficulty == 3:
            total_rounds = 5
        else:
            continue

    clear_screen()
    return total_rounds

def display_round_info(round_number, total_rounds):
    print(f"Round {round_number} of {total_rounds}")


def ask_for_guess():
    guess_str = input("Enter a number between 1 and 100: ")

    clear_screen()

    print("You entered", guess_str)
    return int(guess_str)


def display_hints(guess, secret_number):
    if guess > secret_number:
        print("""You missed! Your guess was bigger than the secret number.
""")
    elif guess < secret_number:
        print("""You missed! Your guess was smaller than the secret number.
""")


def adjust_score(score, guess, secret_number):
    lost_points = abs(secret_number - guess)
    score -= lost_points


if __name__ == "__main__":
    play()
