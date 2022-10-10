import random


def play():
    print("*****************************")
    print("Welcome to the Guessing game!")
    print("*****************************")

    secret_number = random.randrange(1, 101)
    total_rounds = 0
    score = 1000

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

    for round_number in range(1, total_rounds + 1):
        print(f"Round {round_number} of {total_rounds}")

        guess_str = input("Enter a number between 1 and 100: ")
        print("You entered", guess_str)
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("You must enter a number between 1 and 100!")
            continue

        hit = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if hit:
            print(f"You got it right and scored {score} points!")
            break
        else:
            lost_points = abs(secret_number - guess)
            score -= lost_points

            if round_number == total_rounds:
                print(f"The secret number was {secret_number}. You scored {score} points.")
            elif bigger:
                print("You missed! Your guess was bigger than the secret number.")
            elif smaller:
                print("You missed! Your guess was smaller than the secret number.")

    print("Game over")


if __name__ == "__main__":
    play()
