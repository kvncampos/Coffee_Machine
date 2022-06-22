from menu import MENU, resources

money = 2.5
user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
if user_choice == "report":
    for key, value in resources.items():
        if key == "coffee":
            print("{}: {}g".format(key, value).capitalize())
            continue
        print("{}: {}ml".format(key, value).capitalize())
    print(f"Money: ${money}")



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

