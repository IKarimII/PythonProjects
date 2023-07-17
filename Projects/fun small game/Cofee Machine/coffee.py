# TODO 1-  Prompt the user and let them enter their preffered drink
# TODO 2- Check if there is enough recources to make that drink
# TODO 3- Prompt user to enter coins
# TODO 4- Return extra money and check if there is enough money to buy the drink
# TODO 5- Make A report function and off function

from Menu import MENU

profit = 0


def check_for_ingredients():
    resources_used = 0
    for items in MENU[f'{drink}']["ingredients"]:

        if MENU[f'{drink}']["ingredients"][f'{items}'] > resources[f'{items}']:
            print(f"Not Enough", items, ",Please refill the machine")
            return False
        else:
            resources_used += MENU[f'{drink}']["ingredients"][f'{items}']
            resources[f'{items}'] -= resources_used
    return True


def money_checker(total_coins):
    global profit
    change = 0
    if total_coins < MENU[drink]['cost']:
        print("Not enough money")
        return False
    elif total_coins > MENU[drink]['cost']:
        while total_coins > MENU[drink]['cost']:
            total_coins -= 0.01
            change += 0.01
        print(f"You Have Overpaid Your change is: {round(change)}")
        profit += MENU[drink]['cost']
        return True
    else:

        profit += MENU[drink]['cost']
        print("Here is Your Drink")
        return True


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

stopped = False
while not stopped:
    drink = input("What kind of drink would you like? espresso $1.5 / latte $2.5 / cappuccino $3").lower()

    if drink == 'espresso' or drink == 'latte' or drink == 'cappuccino':
        quarters = int(input("How much quarters would you like to insert? $0.25"))
        dimes = int(input("How much dimes would you like to insert? $0.10: >"))
        nickles = int(input("How much nickles would you like to insert? $0.5: >"))
        pennies = int(input("How much pennies would you like to insert? $0.01: >"))

        total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.5 + pennies * 0.01
        check_for_ingredients()
        money_checker(total_money)


    if drink.lower() == 'stop':
        stopped = True
    if drink.lower() == 'report':
        print('profit: ',profit)
        print(resources)
