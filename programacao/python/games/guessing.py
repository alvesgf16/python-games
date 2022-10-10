import random

print("*****************************")
print("Welcome to the Guessing game!")
print("*****************************")

secret_number = random.randrange(1, 101)
total_rounds = 3

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
        print("You're right!")
        break
    else:
        if bigger:
            print("You missed! Your guess was bigger than the secret number.")
        elif smaller:
            print("You missed! Your guess was smaller than the secret number.")

print("Game over")
