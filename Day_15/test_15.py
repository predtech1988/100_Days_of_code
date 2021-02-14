# TODO 
#timemaster, Code Spell Checker
#https://ria.ru/20210209/kazinskiy-1596529577.html
#https://coffee-machine-final.appbrewery.repl.run/
from data import menu
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
total_money = 0
#What would you like? (espresso/latte/cappuccino): report, off
is_running = True


def check_resources(coffee_sort):
    sort = coffee_sort
    ingredients = menu[sort]["ingredients"]
    counter =[]
    for ingredient in ingredients:
        if resources[ingredient] >= ingredients[ingredient]:
            counter.append(True)            
        else:
            print(f"Sorry there is not enough {ingredient}.")
            counter.append(False)  
            break
    if False in counter:
        return False
    else:
        return True

def get_money(coffee_type):
    price = menu[coffee_type]["cost"]
    money = 0
    global total_money
    money += float(input("how many quarters?: ")) * 0.25
    money += float(input("how many dimes?: ")) * 0.10
    money += float(input("how many nickles?: ")) * 0.05
    money += float(input("how many pennies?: ")) * 0.01
    if money < price:
        print("Sorry that's not enough money. Money refunded.")
        money = 0
        return False
    elif money == price:
        total_money += price
        return True
    else:
        change = round(money - price, 2)
        total_money += price
        print(f"Here is ${change} in change.")
        return True

def make_coffee(coffee_type):
    print(f"Making {coffee_type}?")
    if check_resources(coffee_type) and get_money(coffee_type):
        sort = coffee_type
        ingredients = menu[sort]["ingredients"]
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]
        print("Here is your latte ☕️. Enjoy!")
        return True
    else:
        return False

while is_running:
    command  = input("What would you like? ( espresso / latte / cappuccino ): ").lower()
    if command == "off":
        is_running = False
    elif command == "report":        
        for key in resources:
            print(f"{key} {resources[key]} ".title())
        print(f"Money ${total_money}")
            #print(resources[key])
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        is_running = make_coffee(command)
    else:
       print("There is no such command!")
       is_running = False

