from coffee_machine_data import MENU
from coffee_machine_data import resources

resources_in_machine = resources
user_cash = 0.0
ordering = True


def report_resources(res):
    suffix = ""
    for key, value in res.items():
        if key == "water" or key == "milk":
            suffix = "ml"
        else:
            suffix = "g"
        print(f"{key.title()}\t: {value}{suffix}")
    print(f"Money\t: ${user_cash}")


def check_user_input(from_user):
    elements = ["espresso", "latte", "cappuccino", "coffee", "off"]
    if from_user in elements:
        # print("Input correct.")
        return True
    else:
        print("You Have Failed Me.\nTry again.")
        ask_user()
    return False


def add_resources(res, o):
    # if res in ["espresso", "latte", "cappuccino"]:
    #     print(f"{resources_in_machine[res]}")
    resources_in_machine[res] += int(
        input(
            f"Currently in machine {resources_in_machine[res]} for {res} you need {MENU[o]['ingredients'][res]}.\n"
            f"How much you want to add:"))


def add_cash(cash, res, cost):
    money = input(f"How much you want to add? You have: {cash}, {res} cost: {cost}")
    if money.isnumeric():
        money = float(money)
    else:
        add_cash(cash, res, cost)
    return float(money) + user_cash


def warehouse_check(o):
    order_warehouse = {}
    check_order = 0
    for x, y in MENU.items():
        # print(f"{y['ingredients']}")
        if x == o:
            order_warehouse = y['ingredients']
    for x, y in order_warehouse.items():
        # print(f"Check:{x} {y} <= {resources_in_machine[x]}")
        if y <= resources_in_machine[x]:
            check_order += 1
            # print(f"\t\tCheck:{x} {y} <= {resources_in_machine[x]}")
        elif 'y' == input("Do you want to add more stuff? (y/n):").strip().lower():
            add_resources(x, o)
            warehouse_check(o)
    if check_order == 3 or (check_order == 2 and o == 'espresso'):
        return True
    return False


def cash_check(o):
    global user_cash
    order_cost = 0.0
    for x, y in MENU.items():
        # print(f"{y['ingredients']}")
        if x == o:
            order_cost = y['cost']
    if user_cash >= order_cost:
        return True
    else:
        user_cash = add_cash(user_cash, o, order_cost)


def balance_resources(o):
    global user_cash
    order_cost = 0.0
    for x, y in MENU.items():
        # print(f"{y['ingredients']}")
        if x == o:
            order_cost = y['cost']
    user_cash -= order_cost

    order_warehouse = {}
    for x, y in MENU.items():
        # print(f"{y['ingredients']}")
        if x == o:
            order_warehouse = y['ingredients']
    for x, y in order_warehouse.items():
        # print(f"Check:{x} {y} <= {resources_in_machine[x]}")
        resources_in_machine[x] -= MENU[o]['ingredients'][x]
        # print(f"{MENU[o]['ingredients'][x]}")


def dispense_coffee(o):
    if warehouse_check(o) and cash_check(o):
        balance_resources(o)
        print("Here is your latte. Enjoy!")
    return True


def ask_user_coffee():
    input_user = input("What would you like? (espresso/latte/cappuccino):")
    if check_user_input(input_user):
        dispense_coffee(input_user)
    else:
        ask_user_coffee()


def ask_user():
    input_user = input("Coffee / report(off):").lower().strip()
    if input_user == "coffee":
        ask_user_coffee()
    elif input_user == "off":
        report_resources(resources_in_machine)
    if check_user_input(input_user):
        return input_user
    return ""


# print(current_resources_in_machine)
# print(MENU)
while ordering:
    order = ask_user()
    if input("Next customer Y/N:?").strip().lower() == "y":
        ordering = True
    else:
        print("Machine is powering off.")
        ordering = False
