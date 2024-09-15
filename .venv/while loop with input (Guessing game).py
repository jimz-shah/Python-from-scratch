import random
import time

print("Hi, Welcome to guessing game, guess number between 1 and 100")
time.sleep(2)
print("picking a number...")
time.sleep(1)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("No, Guess higher: "))
    else:
        guess = int(input("No, Guess lower: "))
print(f"Yes, it is right. It took you {guess_count} guesses")
