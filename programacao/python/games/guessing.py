print("*****************************")
print("Welcome to the Guessing game!")
print("*****************************")

secret_number = 42
total_rounds = 3
round_number = 1

while round_number <= total_rounds:
    print(f"Round {round_number} of {total_rounds}")
    guess_str = input("Enter your guess: ")
    print("You entered", guess_str)
    guess = int(guess_str)

    hit = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

    if hit:
        print("You're right!")
    else:
        if bigger:
            print("You missed! Your guess was bigger than the secret number.")
        elif smaller:
            print("You missed! Your guess was smaller than the secret number.")

    round_number += 1

print("Game over")
