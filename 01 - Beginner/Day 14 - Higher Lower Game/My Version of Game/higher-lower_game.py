import random
import art
from game_data import data


def compare(first_followers, second_followers):
    """Compares between first account and second account followers and decides if the user got it correct"""
    global game_over, score
    if guess == 'a' and first_followers > second_followers:
        score += 1
        return f"You're right!, Current score: {score}"
    elif guess == 'b' and second_followers > first_followers:
        score += 1
        return f"You're right!, Current score: {score}"
    else:
        game_over = True
        return f"Sorry that's wrong, Final score: {score}"


score = 0
second_data = random.choice(data)
game_over = False
while not game_over:
    # Moving second account data to first account data as the Game Requirements wants.
    first_data = second_data
    second_data = random.choice(data)
    # if the second account data after getting chosen randomly is the same as the account data,
    # we take the random again and again until there are not the same anymore.
    while second_data == first_data:
        second_data = random.choice(data)
    # Formatting prints (didn't do a function for the formatting)
    A = f"{first_data['name']}, a {first_data['description']}, from {first_data['country']}"
    B = f"{second_data['name']}, a {second_data['description']}, from {second_data['country']}"
    # Printing logo of the game
    print(art.logo)

    print(f"Compare A: {A}")
    # Printing the 'VS' art between each account formatted print
    print(art.vs)
    print(f"Against B: {B}")
    # Taking a guess from the user
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # comparing the followers of each account by passing them as parameters and then checking if the user answer is
    # correct to increase the score by 1 and go to next round or end the game
    compare_result = compare(first_data['follower_count'], second_data['follower_count'])
    print(compare_result)
