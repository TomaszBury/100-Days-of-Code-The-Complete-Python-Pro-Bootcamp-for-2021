from coffee_machine_data import MENU
from coffee_machine_data import resources

# print(resources)
# print(MENU)

order = input("What would you like? (espresso/latte/cappuccino):")

print("Please insert coins.")


def check_for_correct_input_coins(coin):
    while not coin.isnumeric():
        coin = input("Only positive numbers:")
    return int(coin)


def check_resources(user_order):
    sufficient_resources = 0
    for key, x in MENU[user_order]['ingredients'].items():
        print(f"Resources: {resources[key]} vs Order: {MENU[user_order]['ingredients'][key]}")
        if MENU[user_order]['ingredients'][key] <= resources[key]:
            # resources[key] = resources[key] - MENU[order]['ingredients'][key]
            # print(f"{resources[key]}")
            sufficient_resources += 1
    if sufficient_resources == 3:
        return "Thank you for your business."
    elif 'y' == input("Do you want add resources to machine? (y/n)"):
        add_resources(user_order)


def add_resources(order):
    if 'y' == input("Do you want to add difference? (y/n)"):
        add_resources_difference(order)
    else:
        for key, x in resources.items():
            resources[key] = resources[key] + int(input(f"How much you want to add? Correctly in machine {resources[key]}"))


def add_resources_difference(order):
    for key, x in MENU[order]['ingredients'].items():
        if MENU[order]['ingredients'][key] > resources[key]:
            resources[key] = MENU[order]['ingredients'][key] - resources[key]


def remove_resources(order):
    for key, x in MENU[order]['ingredients'].items():
        if MENU[order]['ingredients'][key] <= resources[key]:
            # print(f"Resources: {resources[key]} vs Order: {MENU[order]['ingredients'][key]}")
            resources[key] = resources[key] - MENU[order]['ingredients'][key]
            # print(f"{resources[key]}")


def print_order(order):
    for key, x in MENU[order]['ingredients'].items():
        print(f"Resources: {resources[key]} vs Order: {MENU[order]['ingredients'][key]}")


quarters = input("How many quarters?:")
quarters = check_for_correct_input_coins(quarters)

dimes = input("How many dimes?:")
dimes = check_for_correct_input_coins(dimes)

nickles = input("How many nickles?:")
nickles = check_for_correct_input_coins(nickles)

pennies = input("How many pennies?:")
pennies = check_for_correct_input_coins(pennies)


def calculate_amount(quarter, dime, nickle, pennie):
    return (quarter * 25 + dime * 10 + nickle * 5 + pennie) / 100


total_amount = calculate_amount(quarters, dimes, nickles, pennies)

if total_amount >= MENU[order]['cost']:
    print(f"How much money in machine.{total_amount}")
    print(f"{order.title()} is costing: {MENU[order]['cost']}")
    print(f"Place order: {check_resources(order)}")
    print(f"Here is: {total_amount - MENU[order]['cost']:5.2f}$ in change.")
    print(f"Your order:\n {print_order(order)}")
else:
    print("You put not enough.")

# TODO: 1. Print Report of coffee maschine
# TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​”
#           a. Check the user’s input to decide what to do next.
#           b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# print("Hmmm")
