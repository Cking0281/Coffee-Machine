from machine_data import MENU, resources

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


# TODO 3: Print report
def display_report(water, milk, coffee, money):
    """Displays a report to user with all available ingredients."""
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: ${money:.2f}")


# TODO 4: Check resources sufficient?
def resources_sufficient(water, milk, coffee, choice):
    """Checks if enough resources are sufficient for drink and returns True if they are."""
    if water < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif choice != "espresso" and milk < MENU[choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif coffee < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# TODO 5: Process coins
def process_coins(quarters, dimes, nickels, pennies):
    quarters *= QUARTER
    dimes *= DIME
    nickels *= NICKEL
    pennies *= PENNY
    return sum([quarters, dimes, nickels, pennies])


# TODO 6: Check transaction successful
def check_transaction(money, choice):
    if money > MENU[choice]["cost"]:
        leftover_change = money - MENU[choice]["cost"]
        print(f"Here is ${leftover_change:.2f} in change.")
        return MENU[choice]["cost"]
    elif money < MENU[choice["cost"]]:
        print("Sorry that's not enough money. Money refunded.")
        return 0


# TODO 7: Make Coffee
def make_drink(water, milk, coffee, choice):
    """Makes coffee and returns ingredients while displaying a message to user."""
    water -= MENU[choice]["ingredients"]["water"]
    if choice != "espresso":
        milk -= MENU[choice]["ingredients"]["milk"]
    coffee -= MENU[choice]["ingredients"]["coffee"]
    print(f"Here is your {choice}. Enjoy!")
    return water, milk, coffee


def main():
    keep_choosing = True

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = float(0)
    while keep_choosing:
        # TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # TODO 2: Turn off the Coffee Machine by entering "off" to the prompt
        if user_choice == "off":
            keep_choosing = False
        elif user_choice == "report":
            display_report(water, milk, coffee, money)
        elif resources_sufficient(water, milk, coffee, user_choice):
            num_quarters = int(input("how many quarters? "))
            num_dimes = int(input("how many dimes? "))
            num_nickels = int(input("how many nickels? "))
            num_pennies = int(input("how many pennies? "))
            money += check_transaction(process_coins(num_quarters, num_dimes, num_nickels, num_pennies), user_choice)
            water, milk, coffee = make_drink(water, milk, coffee, user_choice)


if __name__ == "__main__":
    main()
