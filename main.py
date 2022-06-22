from menu import MENU, resources
import sys
from time import sleep

money = 2.5


def check_resources():
    ###checks the resources remaining vs needed for coffee###
    drink_selector = user_choice
    print(MENU[drink_selector])

machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "report":
        for key, value in resources.items():
            if key == "coffee":
                print("{}: {}g".format(key, value).capitalize())
                continue
            print("{}: {}ml".format(key, value).capitalize())
        print(f"Money: ${money}")
    elif user_choice == "espresso":
        print("espresso")
    elif user_choice == "latte":
        print("latte")
        check_resources()
    elif user_choice == "cappuccino":
        print("cappuccino")
    elif user_choice == "off":
        choice = input("Are you sure you want to power-off? ").lower()
        if choice == "yes":
            print("Coffee Machine attempting to power off...")
            animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]

            for i in range(100):
                sleep(0.1)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
                # do something
            print("Shutoff Successful!")
            exit()
        else:
            continue
    else:
        print("That's not a valid selection, try again.")

# Coin Operated Machine
# Penny = 1 cent - 0.01
# Nickel = 5 cents - 0.05
# Dime = 10 cents - 0.10
# Quarter = 25 cents - 0.25

# 1.
# Print Report using 'report' to show what resources it has left.

# 2.
# Check resources are sufficient when order is provided.
# It will ask how many of each coin to add, then provide a change amount
# If no resources to make drink, it should state that.

# 3.
# It will ask how many of each coin to add, then provide a change amount
# If not enough money is provided, all money is refunded and no drink given.

# 4.
# check that transaction is successful.

# 5.
# if good. make coffee, and reduce resources available.
