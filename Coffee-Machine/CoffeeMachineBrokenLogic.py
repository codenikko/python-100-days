MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_is_sufficient(choice):
    c = 0
    global will_get_coffee
    for i in ["water","milk","coffee"]:
        if MENU[choice]["ingredients"][i]<=resources[i]:
            resources[i] -= MENU[choice]["ingredients"][i]
        else:
            print(f"Sorry for the inconvenience, out of {i} today!")
            will_get_coffee = False
            break
    

    

    
def process_coins():
    """Returns the total calculated from coins inserted."""

    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total



# Let's tackle the cost part
def tackle_cost():
    money_received = process_coins()
    if money_received > MENU[choice_of_coffee]["cost"] and will_get_coffee == True:
        print(f"Here's' your change of ${round(money_received - MENU[choice_of_coffee]["cost"],2)}")
        print(f"HERE'S YOUR {choice_of_coffee.upper()}")

    elif money_received < MENU[choice_of_coffee]["cost"]:
        print("Insufficient funds, money refunded")

    else:
        print("No change to process")
        print(f"HERE'S YOUR {choice_of_coffee.upper()}")




print("Welcome to the Coffee Vending Machine. ")

want = True
while want == True:
    choice_of_coffee = input("What would you like to have? (espresso/latte/cappuccino) : ").lower()
    print("\n"*4)

    if choice_of_coffee == "resources":
        print(resources)
    else:
        resource_is_sufficient(choice_of_coffee)
        print("\n"*4)



        if not will_get_coffee == False:
            tackle_cost()

    again= input("Do you want another coffee? 'y' for yes 'n' for no")
    if again == "y":
        want = True

    elif again == "n":
        want = False
        
    else:
        print(f"choose correctly! you typed {again}")