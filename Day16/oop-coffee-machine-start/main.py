from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_maker.report()
money_machine.report()

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        break
    elif user_input == "report":
        coffee_maker.report()
    elif user_input in ["espresso", "latte", "cappuccino"]:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
