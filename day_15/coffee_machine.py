from coffee_machine_data import MENU
from coffee_machine_data import resources
from coffee_machine_supply import check_resources

# print(resources)
# print(MENU)

order = input("What would you like? (espresso/latte/cappuccino):")

print("Please insert coins.")


def check_for_correct_input_coins(coin):
    while not coin.isnumeric():
        coin = input("Only positive numbers:")
    return int(coin)


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
    print(f"Do we have all the ingredients. {check_resources(order)}")
    print(f"Here is: {total_amount - MENU[order]['cost']:5.2f}$ in change.")
else:
    print("You put not enough.")

# TODO: 1. Print Report of coffee maschine
# TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​”
#           a. Check the user’s input to decide what to do next.
#           b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# print("Hmmm")
