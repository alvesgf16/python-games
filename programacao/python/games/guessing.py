print("*****************************")
print("Welcome to the Guessing game!")
print("*****************************")

secret_number = 42

guess_str = input("Enter your number: ")

print("You entered", guess_str)

guess = int(guess_str)

if secret_number == int(guess):
    print("You're right!")
else:
    print("You're wrong...")
