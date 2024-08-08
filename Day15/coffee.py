money = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")


def resource_check(coffee_type):
    """Returns True if resources sufficient, otherwise False."""
    for i in coffee_type:
        if coffee_type[i] >= resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def insert_coins():
    """Returns the total calculated coins"""
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is completed. or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Reduce the ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


while True:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "report":
        report()
    elif option == "off":
        break
    elif option in ["espresso", "latte", "cappuccino"]:
        if resource_check(MENU[option]["ingredients"]):
            payment = insert_coins()
            if is_transaction_successful(payment, MENU[option]["cost"]):
                make_coffee(option, MENU[option]["ingredients"])
    else:
        print("Invalid option. Please try again.")
