
import random
secret_number = random.randint(1, 10)

attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a higher number.")

    elif guess > secret_number:
        print("Too high! Try a lower number.")

    else:
        print("🎉 Congratulations! You guessed the number!")
        print("The secret number was:", secret_number)
        print("Total attempts:", attempts)
        break