from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# coffeeMachine = CoffeeMaker()
# menu = Menu()
# money = MoneyMachine()
#
# print(coffeeMachine.report())
#
# print(menu.get_items())
#
# order = input("Your order: ")
#
# menuItem = menu.find_drink(order)
#
# print(f"Name: {menuItem.name}, cost: {menuItem.cost}, ingredients: {menuItem.ingredients}")
#
# if coffeeMachine.is_resource_sufficient(menuItem):
#     print("Resource is sufficient")
#
# if money.make_payment(menuItem.cost):
#     coffeeMachine.make_coffee(menuItem)
#
# print(coffeeMachine.report())
# print(money.report())


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
