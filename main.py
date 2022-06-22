from menu import MENU, resources
import sys
from time import sleep

money = 2.5


def check_resources():
    ###checks the resources remaining vs needed for coffee###
    items_needed = MENU[user_choice]["ingredients"]
    # Testing for accuracy--Delete when project is done
    # print("items Needed", items_needed)
    # print("resources", resources)

    # Subtracting Dictionaries
    ingredients_left = {}
    # Loop key, value for resources, subtract values from each dictionary and add the key/value to ingredients_left
    for k, v in resources.items():
        ingredients_left[k] = v - items_needed.get(k, 0)  # returns value if k exists in d2, otherwise 0

    # stop taking orders when resources <= 0
    flag = True
    out_of_stock = {}
    for temp in ingredients_left.values():
        if temp <= 0:
            flag = False

    if flag:
        return ingredients_left, 0
    # out_of_stock will be used as an input in case you want to find out how many resources are needed to restock
    else:
        out_of_stock = ingredients_left
        return 0, out_of_stock


def shut_off():
    animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]

    for i in range(100):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        # do something
    print("Shutoff Successful!")
    exit()


def left_stock():
    if resources == 0:
        print("No more stock left for this action.")
        refill = input("Do you want to get refill info? ").lower().strip()
        if refill == "yes":
            print("\nIngredients remaining are:\n")
            for key, value in test.items():
                if key == "coffee":
                    print("{}: {}g".format(key, value).capitalize())
                    continue
                print("{}: {}ml".format(key, value).capitalize())
        else:
            exit()
        print("Coffee Machine will now power-off...")
        shut_off()


def report():
    for key, value in resources.items():
        if key == "coffee":
            print("{}: {}g".format(key, value).capitalize())
            continue
        print("{}: {}ml".format(key, value).capitalize())
    print(f"Money: ${money}")


machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "report":
        report()
        # for key, value in resources.items():
        #     if key == "coffee":
        #         print("{}: {}g".format(key, value).capitalize())
        #         continue
        #     print("{}: {}ml".format(key, value).capitalize())
        # print(f"Money: ${money}")

    elif user_choice == "espresso":
        # print("espresso")
        check_resources()
        resources, test = check_resources()
        left_stock()

    elif user_choice == "latte":
        # print("latte")
        check_resources()
        resources, test = check_resources()
        left_stock()

    elif user_choice == "cappuccino":
        # print("cappuccino")
        check_resources()
        resources, test = check_resources()
        left_stock()

    elif user_choice == "off":
        choice = input("Are you sure you want to power-off? ").lower()
        if choice == "yes":
            print("Coffee Machine attempting to power off...")
            shut_off()
        else:
            continue
    else:
        print("That's not a valid selection, try again.")

    # resources = check_resources()
    # if check_resources() == "No more Stock":
    #     print("Testing for empty stock")
    #     exit()
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
