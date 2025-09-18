import random

# Step 1: Generate a random number
secret_number = random.randint(1, 5)

# Step 2: Get user's guess
guess = int(input("Guess a number between 1 and 5: "))

# Step 3: Compare and respond
if guess == secret_number:
    print("Correct! You guessed it.")
else:
    print(f"Wrong! The number was {secret_number}.")