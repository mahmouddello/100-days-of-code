from menu import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(total, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if total >= drink_cost:
        change = round(total - drink_cost, 2)  # Rounded to decimal number
        print(f"Here is the change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def makeCoffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name}! Have a nice day.")


machine_isRunning = True
while machine_isRunning:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        machine_isRunning = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        print(drink)  # prints the drink entry (Value) in my recipes dictionary
        # Accessing the drink's ingredients Key
        if is_resources_sufficient(drink['ingredients']):
            money = process_coins()
            if is_transaction_successful(money, drink['cost']):
                makeCoffee(choice, drink['ingredients'])
