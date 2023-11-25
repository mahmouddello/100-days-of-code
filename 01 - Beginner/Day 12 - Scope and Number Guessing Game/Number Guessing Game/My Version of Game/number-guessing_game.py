from art import logo
import random

x = 5


def attempts_number():
    """Returns how many attempts should user have after choosing the difficulty"""
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    return 0


def guess_game():
    attempts = attempts_number()  # Getting attempt number that has been returned from the function
    secret_number = random.randint(1, 100)  # Random secret number between 1 and 100
    print(f"Psst the number is {secret_number}")
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        if secret_number > guessed_number:
            print("Too low")
            attempts -= 1
        elif secret_number < guessed_number:
            print("Too high")
            attempts -= 1
        else:
            print(f"You got it! The answer was {secret_number}")
            break  # breaking out of while loop if we did a correct guess
        if attempts == 0:
            print(f"You have run out of guesses, you lose.\nThe correct number was {secret_number}.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
guess_game()
