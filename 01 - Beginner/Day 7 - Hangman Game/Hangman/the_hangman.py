# Step 1
import random
import the_hangman_art
import word_list
import click


def clrscr():
    # Clear screen using click.clear() function
    click.clear()


words = word_list.word_full

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Step 2
# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
#  So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter
#  to guess.
# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Step 3
# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
#  all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won
#  #####################################
#  choosing a random word from the list

# Step 4
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
#  TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. If lives goes down to 0 then
#   the game should stop and it should print "You lose.
chosen_word = random.choice(words)
print(the_hangman_art.logo)
# Testing code
print(f"Pssst, the solution is {chosen_word}")
# lives of the hangman game
lives = len(the_hangman_art.stages) - 1
# Creating Blanks, Example : ["_", "_", "_", "_", "_"]
display = (len(chosen_word) * "_ ").split()
end_of_game = False
while not end_of_game:
    # Check guessed letter
    guess = input("guess a letter : ").lower()  # Taking an input and turning the input into a lower case
    if guess in display:
        print(f"You've already guessed {guess}, try again")
        # check if letter has been guessed before
        guess = input("guess a letter : ").lower()
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]  # letter changes in every iteration !
        if letter == guess:
            display[position] = guess
            # replaces the blank space with the guess in the correct position
    if guess not in chosen_word:  # if the guess letter not in the word reduce lives by 1, Notice it's outside the for
        print(f"You guessed {guess}, that's not in the word, you lost a life ")
        print(f"{' '.join(display)}")  # printing display as a string
        lives -= 1
        print(the_hangman_art.stages[lives])  # print out the ASCII art
        if lives == 0:
            end_of_game = True
            print("You lost")
        # if the lives equal to zero that means you lost
    elif "_" not in display:
        end_of_game = True
        print(f"{' '.join(display)}")  # printing display as a string
        print("You win")
        # if there is no more blank spaced in the display that means you won the game
    else:
        print(f"{' '.join(display)}")  # printing display as a string
