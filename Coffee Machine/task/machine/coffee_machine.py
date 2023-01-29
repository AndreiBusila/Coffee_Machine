coffee_machine = {"water": 400,
                  "milk": 540,
                  "beans": 120,
                  "cups": 9,
                  "money": 550
                  }

coffee_features = {"espresso": {"water": 250,
                                "milk": 0,
                                "beans": 16,
                                "cups": 1,
                                "money": 4},

                   "latte": {"water": 350,
                             "milk": 75,
                             "beans": 20,
                             "cups": 1,
                             "money": 7},

                   "cappuccino": {"water": 200,
                                  "milk": 100,
                                  "beans": 12,
                                  "cups": 1,
                                  "money": 6}
                   }

type_coffee = ("espresso", "latte", "cappuccino")


def make_coffee(coffee):
    coffee_machine["water"] = coffee_machine["water"] - coffee_features[coffee]["water"]
    coffee_machine["milk"] = coffee_machine["milk"] - coffee_features[coffee]["milk"]
    coffee_machine["beans"] = coffee_machine["beans"] - coffee_features[coffee]["beans"]
    coffee_machine["cups"] = coffee_machine["cups"] - coffee_features[coffee]["cups"]
    coffee_machine["money"] = coffee_machine["money"] + coffee_features[coffee]["money"]


def verify_resources(coffee):
    if coffee_machine["water"] < coffee_features[coffee]["water"]:
        print("Sorry, not enough water!")
        return False
    if coffee_machine["milk"] < coffee_features[coffee]["milk"]:
        print("Sorry, not enough milk!")
        return False
    if coffee_machine["beans"] < coffee_features[coffee]["beans"]:
        print("Sorry, not enough beans!")
        return False
    if coffee_machine["cups"] < coffee_features[coffee]["cups"]:
        print("Sorry, not enough cups!")
        return False
    return True


def buy_coffee():
    action = input("What do you want to buy? "
                   "1 - espresso, "
                   "2 - latte, "
                   "3 - cappuccino, "
                   "back - to main menu:\n")
    if action == "back":
        return 0
    action = int(action) - 1
    if verify_resources(type_coffee[action]):
        print("I have enough resources, making you a coffee!")
        make_coffee(type_coffee[action])


def fill_machine():
    coffee_machine["water"] = coffee_machine["water"] \
                              + int(input("Write how many ml of water you want to add:\n"))
    coffee_machine["milk"] = coffee_machine["milk"] \
                             + int(input("Write how many ml of milk you want to add:\n"))
    coffee_machine["beans"] = coffee_machine["beans"] \
                              + int(input("Write how many grams of coffee beans you want to add:\n"))
    coffee_machine["cups"] = coffee_machine["cups"] \
                             + int(input("Write how many disposable cups you want to add:\n"))
    print()


def take_money():
    print("I gave you ${0}".format(coffee_machine["money"]))
    coffee_machine["money"] = 0
    print()


def remaining():
    print("\nThe coffee machine has:")
    print("{0} ml of water".format(coffee_machine["water"]))
    print("{0} ml of milk".format(coffee_machine["milk"]))
    print("{0} g of coffee beans".format(coffee_machine["beans"]))
    print("{0} disposable cups".format(coffee_machine["cups"]))
    print("${0} of money\n".format(coffee_machine["money"]))


def make_action(action):
    if action == "buy":
        buy_coffee()
        print()
    elif action == "fill":
        fill_machine()
    elif action == "take":
        take_money()
    elif action == "remaining":
        remaining()


def main():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "exit":
            break
        make_action(action)


main()
