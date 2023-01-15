from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while is_on:
    options = menu.get_items()
    choice = input(f"​What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            machine.make_coffee(drink)