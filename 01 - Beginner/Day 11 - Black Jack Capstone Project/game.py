import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated form the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        # Black Jack ! Ace + (10, J, Q, K)
    if 11 in cards and sum(cards) > 21:
        # If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares your score and the Computer's score and decides the result of the game"""
    if user_score > 21 and computer_score > 21:
        return 'You both want over. You lose'

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def playGame():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        # Dealing two random card from the deck for both user and computer
    while not is_game_over:
        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
        # then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your score is {user_score} with cards : {user_cards}")
        print(f"Computer's score is {computer_score} with cards : {computer_cards}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    playGame()
