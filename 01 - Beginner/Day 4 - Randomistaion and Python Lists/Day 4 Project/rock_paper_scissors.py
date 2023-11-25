import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, you lose!")
# moved all conditions under else, so we jump over out of index and undefined variables problems.
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose")
    print(game_images[computer_choice])
    # base case to run the whole program
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
        # user = rock , computer = scissors >> user win
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        # computer = rock ,user = scissors  >> computer win
    elif computer_choice > user_choice:
        print("You lose")
        # user = paper , computer = scissors >> computer win
    elif user_choice > computer_choice:
        print("You win!")
        # user = scissors , computer = paper >> user win
    elif computer_choice == user_choice:
        print("It's a draw")
        # Draw
