from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()  # Object from CoffeeMaker Class
machine_isRunning = True
drinks_menu = Menu()  # Object from menu class
moneyMachine = MoneyMachine()
options = drinks_menu.get_items()
while machine_isRunning:
    choice = input(f"What would you like? {options}")
    if choice == 'off':
        machine_isRunning = False
    elif choice == 'report':
        moneyMachine.report()
        coffeeMaker.report()
    else:
        drink = drinks_menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
