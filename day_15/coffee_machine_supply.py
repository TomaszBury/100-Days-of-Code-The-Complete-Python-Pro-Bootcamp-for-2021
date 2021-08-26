from coffee_machine_data import resources, MENU


def check_resources(order):
    sufficient_resources = 0
    for key, x in MENU[order]['ingredients'].items():
        if MENU[order]['ingredients'][key] <= resources[key]:
            # print(f"Resources: {resources[key]} vs Order: {MENU[order]['ingredients'][key]}")
            resources[key] = resources[key] - MENU[order]['ingredients'][key]
            # print(f"{resources[key]}")
            sufficient_resources += 1
    return sufficient_resources == 3
