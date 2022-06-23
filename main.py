from menu import MENU, resources
import sys
from time import sleep

money_in_machine = 0


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


def fetching_drink():
    print("Fetching drink ingredients")
    animation = ["-", " -", "  -"]

    for i in range(100):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    #



def left_stock():
    if resources == 0:
        print("Alert: Machine has no more ingredients left for this drink order\n")
        refill = input("Do you want to get refill info? ").lower().strip()
        if refill == "yes":
            print("\nIngredients remaining are:\n")
            for key, value in test.items():
                if key == "coffee":
                    print("{}: {}g".format(key, value).capitalize())
                    continue
                print("{}: {}ml".format(key, value).capitalize())
            turn_off_coffee: input("Do you want to power off machine?").lower()
            if turn_off_coffee == "yes":
                print("Coffee Machine will now power-off...")
                shut_off()
        else:
            turn_off_coffee: input("Do you want to power off machine?").lower()
            if turn_off_coffee == "yes":
                print("Coffee Machine will now power-off...")
                shut_off()

    else:
        print(f"Your {user_choice} is Ready. Enjoy!!!")


def report():
    print("\nThe Current Status Inventory is: ")
    for key, value in resources.items():
        if key == "coffee":
            print("{}: {}g".format(key, value).capitalize())
            continue
        print("{}: {}ml".format(key, value).capitalize())
    print(f"Money: ${money_in_machine}\n")


def item_price(drink, quarter, dime, nickel, pennie):
    """Provides Cost of Drink, Difference in price"""
    global money_in_machine
    if money_in_machine < 0:
        print("Not enough money in machine.")
        exit()
    # Gives cost of Drink and subtracts money given
    item_cost = MENU[drink]["cost"]
    # print(f"\n{drink} costs: ${item_cost}")
    total_coin_deposit = [float(quarters) * .25, float(dimes) * .10, float(nickels) * .05, float(pennies) * .01]
    money_inserted = 0
    for coin in total_coin_deposit:
        money_inserted += coin

    coin_value = {
        "quarter": .25,
        "dime": .10,
        "nickel": .05,
        "penny": .01,
    }

    if money_inserted > item_cost:
        difference = money_inserted - item_cost
        print(f"Here is your refund of ${format(difference, '.2f')}")
        money_in_machine += item_cost
        fetching_drink()
        return "success"

    elif money_inserted == item_cost:
        print(money_in_machine)
        money_in_machine += item_cost
        print(money_in_machine)
        fetching_drink()
        return "success"

    else:
        myfloat = item_cost - money_inserted
        print("That's not enough money.\n")
        print(f"You inserted ${money_inserted} and are missing ${format(myfloat, '.2f')}\nYour money will be refunded.")
        print("\nTry again, please.")
        return "fail"


machine_on = True

while machine_on:
    flag = True
    while flag:
        user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
        if user_choice not in ["report", "latte", "espresso", "cappuccino"]:
            print("That's not valid entry, try again.")
            continue
        else:
            flag = False

    if user_choice == "report":
        report()
        # Add a clear function/module so this report disappears after a delay
        continue
    # Provide cost of Menu Item
    print("The price of this item is: $", MENU[user_choice]["cost"])

    # Currency Check and Sum of Difference.
    print("Please insert coins.")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickels = input("how many nickels? ")
    pennies = input("how many pennies?: ")

    if user_choice == "espresso":
        # print("espresso")
        item_price(user_choice, quarters, nickels, dimes, pennies)
        check_resources()
        resources, test = check_resources()
        if test == 0:
            print("Purchase Successful...Testing")
        left_stock()
        # if item_price(user_choice, quarters, nickels, dimes, pennies) == "success".lower():
        #     print(f"Here is your {user_choice}. Enjoy!")
        # might delete bottom and move to report only...
        print("Current Money in Machine: $", money_in_machine)

    elif user_choice == "latte":
        # print("latte")
        item_price(user_choice, quarters, nickels, dimes, pennies)
        check_resources()
        resources, test = check_resources()
        left_stock()

        # might delete bottom and move to report only...
        print("Current Money in Machine: $", money_in_machine)

    elif user_choice == "cappuccino":
        # print("cappuccino")
        item_price(user_choice, quarters, nickels, dimes, pennies)
        check_resources()
        resources, test = check_resources()
        left_stock()

        # might delete bottom and move to report only...
        print("Current Money in Machine: $", money_in_machine)

    elif user_choice == "off":
        choice = input("Are you sure you want to power-off? ").lower()
        if choice == "yes":
            print("Coffee Machine attempting to power off...")
            shut_off()
        else:
            continue
    else:
        print("That's not a valid selection, try again.")

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
