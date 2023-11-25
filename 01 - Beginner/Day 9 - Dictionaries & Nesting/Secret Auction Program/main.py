from art import logo

print(logo)

# Create an empty dictionary
bids = {}
# Create a flag to control the loop
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    # We need to loop on the bidding_record dictionary
    for bidder in bidding_record:
        # Remember that looping over a dictionary like this getting us the KEYS
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name: ")
    bid_price = int(input("What's your bid? $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if should_continue == 'no':
        bidding_finished = True
        print('\n' * 100)
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print('\n' * 100)
    else:
        bidding_finished = True
        print('\n' * 100)
        find_highest_bidder(bids)
