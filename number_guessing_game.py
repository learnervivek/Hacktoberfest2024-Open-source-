import random

def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    print("Welcome to the number guessing game!")
    print("Guess a number between 1 and 10.")

    # Loop until the user guesses correctly
    while True:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
            
            # Check if the guess is within the correct range
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low, try again!")
            elif guess > secret_number:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You've guessed the correct number: {secret_number}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
# Start the game
guess_number()
