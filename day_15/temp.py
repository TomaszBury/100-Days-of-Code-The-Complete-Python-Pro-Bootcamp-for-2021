from coffee_machine_data import resources, MENU


# def check_resources(user_order):
#     sufficient_resources = 0
#     for key, x in MENU[user_order]['ingredients'].items():
#         print(f"Resources: {resources[key]} vs Order: {MENU[user_order]['ingredients'][key]}")
#         if MENU[user_order]['ingredients'][key] <= resources[key]:
#             # resources[key] = resources[key] - MENU[order]['ingredients'][key]
#             # print(f"{resources[key]}")
#             sufficient_resources += 1
#     if sufficient_resources == 3:
#         return "Thank you for your business."
#     # elif 'y' == input("Do you want add resources to machine? (y/n)"):
#     #     add_resources(user_order)
#     return "Done"
#
#
# order = "cappuccino"
#
# print(f"Place order: {check_resources(order)}")

current_resources_in_machine = resources

# print(f"{current_resources_in_machine}")

# for key, x in current_resources_in_machine.items():
#     print(f"key: {key}, resources: {x}")

