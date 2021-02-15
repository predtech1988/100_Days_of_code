from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
makers = CoffeeMaker()
money = MoneyMachine()
is_continue =True


while is_continue:
    order = input(f"What would you like? {my_menu.get_items()}")
    ordered_drink = my_menu.find_drink(order)
    if ordered_drink:
        if (makers.is_resource_sufficient(ordered_drink)) and money.make_payment(ordered_drink.cost):
            makers.make_coffee(ordered_drink)
    elif order == "off":
        is_continue = False        
    elif order == "report":
        makers.report()
        money.report()
    else:
        print("Something Went wrong with command.")